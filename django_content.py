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
]
