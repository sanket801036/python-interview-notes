"""Content for Django_Interview_Theory.docx.

Level: 3-year-experience answers - not beginner definitions. Each topic still
uses simple English, but the content goes to the depth an interviewer expects
from someone with production Django behind them. Small example per topic.
Add one phase at a time, then run:  python build_docx.py django
"""

DOC_TITLE = "Django Interview Theory Notes"
DOC_SUBTITLE = "3-year-experience depth  |  Simple English + examples  |  Sanket Kolhe"

CONTENT = [
    {
        "phase": "Django Phase 1 - Core Architecture",
        "topics": [
            {
                "title": "D1.1  What is Django - MTV and Batteries Included",
                "what": "Django is a high-level Python web framework that ships with everything a serious app needs: ORM, auth, admin, migrations, security.",
                "points": [
                    "\"Batteries included\": ORM, migrations, authentication, admin panel, forms, caching, security middleware - all built in. Flask/FastAPI leave these to libraries we assemble ourselves.",
                    "MTV = Model, Template, View. Same idea as MVC with renamed parts: Model = data (MVC model), View = business logic (MVC controller), Template = presentation (MVC view). Django's URL dispatcher plays the router.",
                    "Design philosophy: DRY (define a model once - migrations, admin, forms all derive from it) and convention over configuration.",
                    "Built for fast, safe development: the admin alone replaces weeks of internal-tool work.",
                    "Where it fits: content sites, dashboards, standard CRUD/REST backends. Where it fights us: highly async workloads, tiny microservices - there FastAPI is leaner.",
                    "Scales fine in practice (Instagram, YouTube-scale usage) - the bottleneck is almost always the database, not the framework.",
                ],
                "example": "django-admin startproject shop\npython manage.py startapp orders\npython manage.py runserver",
                "answer": "Django is a batteries-included Python framework following MTV - model for data, view for logic, template for presentation, with the URL dispatcher routing. Its DRY design means one model definition drives migrations, admin and forms. I pick Django for full-featured backends and admin-heavy products, and FastAPI when I need lean async APIs.",
            },
            {
                "title": "D1.2  Request/Response Cycle",
                "what": "Every request flows: web server -> WSGI/ASGI -> middleware (down) -> URL resolver -> view -> middleware (up) -> response.",
                "points": [
                    "Production entry: nginx receives the request and proxies to gunicorn/uwsgi, which speaks WSGI to Django (or uvicorn speaking ASGI for async).",
                    "Django builds an HttpRequest object, then runs the request through the MIDDLEWARE list top-down (security, sessions, auth attach request.user here).",
                    "The URL resolver matches the path against urlpatterns and picks a view, passing captured parameters.",
                    "The view runs business logic - ORM queries, serialization - and returns an HttpResponse (or raises, and exception middleware turns it into an error response).",
                    "The response passes back up the middleware stack bottom-up (so a middleware can time or modify both sides), then goes out through WSGI to the client.",
                    "Knowing this order explains real bugs: request.user missing means auth middleware order is wrong; CORS headers missing means that middleware is too low.",
                ],
                "example": "Browser -> nginx -> gunicorn (WSGI)\n -> SecurityMiddleware -> SessionMiddleware\n -> AuthenticationMiddleware -> URL resolver\n -> view -> ORM -> HttpResponse\n -> back up middleware -> client",
                "answer": "nginx hands the request to gunicorn, which calls Django through WSGI. Django runs middleware top-down - sessions and auth attach request.user - resolves the URL to a view, the view does the work and returns a response, which travels back up the middleware stack. Middleware order matters: auth issues and missing headers usually trace back to it.",
            },
            {
                "title": "D1.3  Project vs App and Settings",
                "what": "A project is the whole site (settings + root urls); an app is one self-contained feature module - a project holds many apps.",
                "points": [
                    "Project folder: settings.py, root urls.py, wsgi.py/asgi.py. App folder: models.py, views.py, urls.py, admin.py, tests.py, migrations/.",
                    "Apps keep code modular and reusable: an 'orders' app, a 'payments' app - each owns its models and URLs. INSTALLED_APPS registers them.",
                    "Real-world settings are split per environment: base.py + dev.py + prod.py, or one settings.py driven by environment variables.",
                    "Secrets (SECRET_KEY, DB password, API keys) never live in code - environment variables or a .env via django-environ.",
                    "DEBUG=True must never reach production: it leaks stack traces and settings on every error page.",
                    "Key settings to know: DATABASES, ALLOWED_HOSTS, MIDDLEWARE, TEMPLATES, STATIC_/MEDIA_ROOT, CACHES.",
                ],
                "example": "shop/            # project\n  settings/base.py, dev.py, prod.py\n  urls.py\norders/          # app\n  models.py views.py urls.py admin.py\nSECRET_KEY = os.environ[\"SECRET_KEY\"]",
                "answer": "The project is the site-level configuration; apps are pluggable feature modules with their own models, views and URLs, registered in INSTALLED_APPS. In production I split settings per environment, feed secrets from environment variables, and never ship DEBUG=True - it leaks stack traces and config.",
            },
            {
                "title": "D1.4  URL Routing",
                "what": "urlpatterns map URL paths to views; include() nests each app's URLs, and names make URLs reversible.",
                "points": [
                    "path(\"orders/<int:pk>/\", views.order_detail, name=\"order-detail\") - the converter (<int:pk>) validates and casts, passing pk into the view.",
                    "Converters: int, str, slug, uuid, path. re_path() takes a regex when converters are not enough.",
                    "Root urls.py include()s app urls: path(\"api/orders/\", include(\"orders.urls\")) - apps stay self-contained.",
                    "Never hardcode URLs: reverse(\"order-detail\", args=[5]) in Python, {% url %} in templates - renaming paths then breaks nothing.",
                    "app_name = \"orders\" adds a namespace: reverse(\"orders:order-detail\") - avoids name clashes between apps.",
                    "Order matters: first match wins, top to bottom.",
                ],
                "example": "# orders/urls.py\napp_name = \"orders\"\nurlpatterns = [\n  path(\"<int:pk>/\", views.detail, name=\"detail\"),\n]\n# usage\nreverse(\"orders:detail\", args=[5])  # /api/orders/5/",
                "answer": "urlpatterns map paths to views with typed converters like <int:pk>, apps keep their own urls.py pulled in with include(), and named routes plus namespaces let me build URLs with reverse() instead of hardcoding. Matching is top-down, first hit wins.",
            },
            {
                "title": "D1.5  FBV vs CBV",
                "what": "Function-based views are plain functions per request; class-based views organize behavior in classes with methods per HTTP verb and heavy reuse via mixins.",
                "points": [
                    "FBV: def order_list(request): explicit, readable, all logic visible in one place. if request.method == \"POST\" branches by hand.",
                    "CBV: class OrderList(View) with get()/post() methods - the verb dispatch is automatic.",
                    "Generic CBVs (ListView, DetailView, CreateView) implement whole CRUD patterns in a few lines - queryset + template and done.",
                    "CBV power = mixins (LoginRequiredMixin etc.) and overridable hooks (get_queryset, get_context_data).",
                    "CBV cost: logic spreads across parent classes - debugging means knowing the method resolution order; over-customized CBVs get harder to follow than an explicit FBV.",
                    "Working rule: generic CRUD -> CBV; unusual or branching logic -> FBV. In DRF the same idea appears as APIView vs generics vs ViewSets.",
                ],
                "example": "class OrderList(ListView):\n    model = Order\n    paginate_by = 20\n    def get_queryset(self):\n        return Order.objects.filter(\n            user=self.request.user)",
                "answer": "FBVs are explicit functions - best when logic is custom; CBVs dispatch by HTTP method and shine with generic views and mixins for standard CRUD, at the cost of logic hidden in the class hierarchy. I use generics for plain CRUD and drop to FBVs for complex flows - same trade-off as DRF's ViewSets vs APIView.",
            },
            {
                "title": "D1.6  Templates (short)",
                "what": "Django's template language renders HTML with variables, tags and filters, kept deliberately logic-light.",
                "points": [
                    "{{ variable }} outputs a value, {% tag %} runs logic (for, if, block), {{ value|filter }} transforms (date, upper, default).",
                    "Template inheritance: base.html defines {% block %}s; child templates extend and fill them - one layout, many pages.",
                    "Auto-escaping is ON: variables are HTML-escaped by default, which blocks XSS. |safe disables it - only for trusted content.",
                    "Business logic stays in views/models; templates only display. No arbitrary Python in templates - by design.",
                    "{% csrf_token %} inside forms pairs with CSRF middleware.",
                    "As an API developer: DRF responses skip templates entirely - but the admin, emails and error pages still use them.",
                ],
                "example": "{% extends \"base.html\" %}\n{% block content %}\n  {% for o in orders %}\n    <p>{{ o.id }} - {{ o.amount|floatformat:2 }}</p>\n  {% endfor %}\n{% endblock %}",
                "answer": "Django templates render display-only HTML with variables, tags and filters, plus inheritance through blocks for shared layouts. Auto-escaping is on by default, which prevents XSS unless someone marks content |safe. In API work I rarely touch them, but admin and transactional emails still run on templates.",
            },
        ],
    },
    {
        "phase": "Django Phase 2 - Models and ORM",
        "topics": [
            {
                "title": "D2.1  Models and Migrations",
                "what": "A model is a Python class mapped to one database table; migrations are versioned files that evolve the schema to match the models.",
                "points": [
                    "Each attribute is a field (CharField, DecimalField, ForeignKey...) mapping to a column; Django adds an auto id primary key unless we define one.",
                    "Flow: edit models -> makemigrations (writes a migration file from the diff) -> migrate (applies pending ones, recorded in the django_migrations table).",
                    "Migrations are code: committed to git, reviewed, run identically on every environment - that is the whole point.",
                    "sqlmigrate shows the SQL a migration will run; --fake marks one applied without running (for syncing weird states).",
                    "Data migrations (RunPython) transform existing rows during schema changes - e.g. filling a new column.",
                    "Production care: adding NOT NULL without default needs a two-step migration; huge-table ALTERs can lock - plan them.",
                    "Meta options worth knowing: db_table, ordering, indexes, constraints, unique_together.",
                ],
                "example": "class Order(models.Model):\n    customer = models.ForeignKey(\"Customer\",\n        on_delete=models.CASCADE)\n    amount = models.DecimalField(max_digits=10,\n        decimal_places=2)\n    class Meta:\n        indexes = [models.Index(fields=[\"customer\"])]\n# python manage.py makemigrations && migrate",
                "answer": "Models map classes to tables; makemigrations diffs the models into versioned migration files and migrate applies them, tracked in django_migrations. They live in git so every environment evolves identically. At 3 years I also know data migrations with RunPython, sqlmigrate to preview SQL, and that NOT NULL additions and big-table ALTERs need care in production.",
            },
            {
                "title": "D2.2  QuerySet - Lazy Evaluation and Caching",
                "what": "A QuerySet is a lazy description of a query - no SQL runs until the data is actually needed, and results are then cached on that QuerySet.",
                "points": [
                    "qs = Order.objects.filter(status=\"paid\") runs NOTHING. Chaining more filters still runs nothing - each returns a new QuerySet.",
                    "Evaluation triggers: iterating (for), list(), len(), bool()/if, slicing with a step, repr, serialization.",
                    "After first evaluation the results cache inside the QuerySet - looping it twice hits the DB once.",
                    "Trap: two separate expressions (qs.count() then list(qs)... or building qs twice) are separate queries - assign once and reuse.",
                    "exists() and count() are cheaper than len(list(qs)) when we only need a check or a number.",
                    "values()/values_list() fetch dicts/tuples instead of model objects - lighter for reports; only() and defer() control columns.",
                    "iterator() streams rows without caching - for processing millions of rows without eating RAM.",
                ],
                "example": "qs = Order.objects.filter(status=\"paid\")  # no SQL yet\nif qs.exists():          # cheap EXISTS query\n    total = qs.count()   # COUNT query\n    for o in qs:         # SELECT + cache\n        ...\n    for o in qs:         # cached - no new query",
                "answer": "QuerySets are lazy - filters just build the query, and SQL runs only on iteration, list(), len() or bool(), after which results cache on that object. I use exists() and count() for cheap checks, values_list() for light reads, iterator() for huge datasets, and I reuse one evaluated queryset instead of re-evaluating.",
            },
            {
                "title": "D2.3  select_related vs prefetch_related - The N+1 Problem",
                "what": "N+1 means one query for the list plus one more per row for its relation; select_related and prefetch_related collapse that into 1-2 queries.",
                "points": [
                    "The bug: for o in Order.objects.all(): print(o.customer.name) - 1 query for orders + 1 per order for its customer. 200 orders = 201 queries.",
                    "select_related(\"customer\"): SQL JOIN, one query. For single-valued relations - ForeignKey and OneToOne.",
                    "prefetch_related(\"items\"): two queries (parents, then all children WHERE parent_id IN (...)), joined in Python. For multi-valued - ManyToMany and reverse FK.",
                    "Both chain and mix: Order.objects.select_related(\"customer\").prefetch_related(\"items\").",
                    "Prefetch(queryset=...) customizes the prefetch - filter or select_related inside it.",
                    "Follow relations with __: select_related(\"customer__city\").",
                    "This is THE classic Django performance interview question - name the symptom (page slow, query count huge) and the fix.",
                ],
                "example": "# 201 queries:\nfor o in Order.objects.all():\n    print(o.customer.name)\n# 1 query:\nfor o in Order.objects.select_related(\"customer\"):\n    print(o.customer.name)\n# M2M: 2 queries\nOrder.objects.prefetch_related(\"items\")",
                "answer": "N+1 is one list query plus a query per row for its relation. select_related fixes single-valued relations (FK, OneToOne) with a JOIN in one query; prefetch_related fixes multi-valued ones (M2M, reverse FK) with a second IN-query stitched in Python. I spot it via query counts in debug toolbar and fix it at the queryset.",
            },
            {
                "title": "D2.4  F Objects, Q Objects and Aggregation",
                "what": "F references a column inside the query, Q builds OR/NOT conditions, and aggregate/annotate compute values in the database.",
                "points": [
                    "F avoids race conditions: Product.objects.filter(id=5).update(stock=F(\"stock\") - 1) - the DB does the maths atomically; read-modify-save in Python loses concurrent updates.",
                    "F also compares columns to each other: filter(sold=F(\"stock\")).",
                    "Q enables OR and NOT, which plain filter kwargs (always AND) cannot: filter(Q(status=\"new\") | Q(priority=\"high\")), and ~Q for negation.",
                    "aggregate() collapses the whole queryset to one dict: aggregate(total=Sum(\"amount\")).",
                    "annotate() adds a computed value PER ROW/group: Customer.objects.annotate(order_count=Count(\"order\")) - then filter or order by it.",
                    "annotate + values gives GROUP BY reports; functions: Count, Sum, Avg, Min, Max, plus Case/When for conditional aggregates.",
                    "All of this runs in the database - almost always faster than looping in Python.",
                ],
                "example": "Product.objects.filter(pk=5).update(\n    stock=F(\"stock\") - 1)          # atomic\nOrder.objects.filter(\n    Q(status=\"new\") | Q(amount__gt=5000))\nCustomer.objects.annotate(\n    n=Count(\"order\")).filter(n__gt=10)",
                "answer": "F pushes column references into SQL - update(stock=F('stock')-1) is atomic and race-free, unlike read-modify-save. Q composes OR/NOT conditions that keyword filters can't. aggregate gives one summary row, annotate computes per row or group for filtering and ordering - all executed in the database where it belongs.",
            },
            {
                "title": "D2.5  Relationships - FK, OneToOne, ManyToMany",
                "what": "ForeignKey is many-to-one, OneToOneField is one-to-one, ManyToManyField creates a junction table - with related_name controlling the reverse side.",
                "points": [
                    "ForeignKey(Customer, on_delete=...): many orders per customer. on_delete is mandatory: CASCADE (delete children), PROTECT (block), SET_NULL (needs null=True).",
                    "PROTECT is the safe default for business data - accidental parent deletes fail loudly instead of silently wiping children.",
                    "OneToOneField: profile-per-user pattern; access both ways as single objects.",
                    "ManyToManyField: Django creates the join table; through=\"Membership\" replaces it with our own model when the relation itself has fields (date joined, role).",
                    "Reverse access: customer.order_set by default; related_name=\"orders\" renames it (customer.orders.all()).",
                    "related_name=\"+\" disables the reverse when it is never needed.",
                    "Self-relations: ForeignKey(\"self\") builds trees (category parent); M2M to self builds graphs (followers, symmetrical=False).",
                ],
                "example": "class Order(models.Model):\n    customer = models.ForeignKey(Customer,\n        on_delete=models.PROTECT,\n        related_name=\"orders\")\n    tags = models.ManyToManyField(Tag, blank=True)\n# customer.orders.all(), tag.order_set.all()",
                "answer": "FK models many-to-one with a mandatory on_delete - I default to PROTECT for business data; OneToOne is the profile pattern; M2M builds a junction table, replaced by a through model when the relation carries its own fields. related_name names the reverse accessor, and self-referencing FKs model hierarchies.",
            },
            {
                "title": "D2.6  Model Inheritance - Abstract, Multi-table, Proxy",
                "what": "Django offers three inheritance styles: abstract (shared fields, no extra table), multi-table (each class a table), proxy (same table, new behavior).",
                "points": [
                    "Abstract base (Meta: abstract = True): children copy its fields into their own tables; the base has no table. The workhorse - TimeStampedModel with created/updated used everywhere.",
                    "Multi-table: both parent and child get tables joined by an implicit OneToOne. Every child query joins - a hidden performance cost people forget. Rarely the right choice.",
                    "Proxy (Meta: proxy = True): no new table, no new fields - just different Python behavior: custom manager, different ordering, extra methods on the same data.",
                    "Choosing: share common fields -> abstract; genuinely need parent-level querying across subtypes -> multi-table (or reconsider: one table + type field); same data, different behavior -> proxy.",
                    "Interviewers probe multi-table because of the surprise JOINs and the parent_ptr link.",
                ],
                "example": "class TimeStamped(models.Model):\n    created = models.DateTimeField(auto_now_add=True)\n    updated = models.DateTimeField(auto_now=True)\n    class Meta:\n        abstract = True\nclass Order(TimeStamped): ...  # own table only",
                "answer": "Abstract bases copy shared fields into each child's table - my default for things like timestamps. Multi-table inheritance gives every class a table linked by OneToOne, silently JOINing on each child query, so I avoid it unless cross-type querying truly pays. Proxy models reuse the same table with different behavior - managers, ordering, methods.",
            },
            {
                "title": "D2.7  Transactions - atomic and select_for_update",
                "what": "transaction.atomic wraps DB work in all-or-nothing blocks, and select_for_update row-locks data against concurrent edits.",
                "points": [
                    "Default Django mode is autocommit - every ORM write commits alone. Multi-step operations need explicit grouping.",
                    "with transaction.atomic(): everything inside commits together or rolls back on exception. Also usable as a decorator.",
                    "atomic blocks nest - inner blocks become savepoints, so an inner failure can roll back partially.",
                    "ATOMIC_REQUESTS=True wraps every request in a transaction - simple, but holds transactions longer under load.",
                    "select_for_update() adds FOR UPDATE - other transactions wait for the lock: the fix for stock/wallet race conditions. Must run inside atomic.",
                    "F() expressions are the lighter alternative for simple counters; select_for_update is for read-then-decide logic.",
                    "on_commit(callback) delays side effects (emails, Celery tasks) until after commit - so a rollback cannot leave a task pointing at data that never got saved.",
                ],
                "example": "with transaction.atomic():\n    p = (Product.objects\n         .select_for_update().get(pk=5))\n    if p.stock > 0:\n        p.stock -= 1\n        p.save()\ntransaction.on_commit(lambda:\n    notify_task.delay(p.id))",
                "answer": "transaction.atomic makes a block all-or-nothing with savepoints when nested; select_for_update inside it row-locks against races - my pattern for stock and payment flows, with F() expressions for simple atomic counters. on_commit defers emails and Celery tasks until the data is truly committed.",
            },
            {
                "title": "D2.8  Custom Managers and QuerySets",
                "what": "A custom QuerySet holds reusable, chainable query logic; a manager exposes it as the model's entry point (objects).",
                "points": [
                    "Problem: filter(status='active', deleted_at__isnull=True) copy-pasted through the codebase - one rule change touches twenty files.",
                    "Solution: methods on a custom QuerySet - Order.objects.paid().recent().for_customer(c) - named business language, chainable.",
                    "Wiring: OrderQuerySet.as_manager(), or a Manager whose get_queryset() returns the custom QuerySet.",
                    "Default-filtering managers (e.g. auto-hiding soft-deleted rows) are risky: admin and shell silently miss data. Keep objects honest; add a separate manager or explicit methods for filtered views.",
                    "The first declared manager is the default one used by admin and dumpdata - order matters.",
                    "This is the standard 'fat model, thin view' pattern - query logic lives at the data layer where it is testable.",
                ],
                "example": "class OrderQuerySet(models.QuerySet):\n    def paid(self):\n        return self.filter(status=\"paid\")\n    def recent(self):\n        return self.order_by(\"-created\")[:50]\nclass Order(models.Model):\n    objects = OrderQuerySet.as_manager()\n# Order.objects.paid().recent()",
                "answer": "I put reusable filters on a custom QuerySet and expose it via as_manager, so queries read like business language and stay chainable - Order.objects.paid().recent(). I avoid default managers that silently hide rows (soft-delete traps admin and shell); explicit methods are safer, and the first manager declared is the default the admin uses.",
            },
        ],
    },
]
