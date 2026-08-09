"""Content for FastAPI_Interview_Theory.docx.

Compact set - FastAPI-specific topics only; web concepts already covered in the
Django notes are not repeated. 3-YOE depth, simple English, example per topic.
Run:  python build_docx.py fastapi
"""

DOC_TITLE = "FastAPI Interview Theory Notes"
DOC_SUBTITLE = "Compact / FastAPI-specific  |  3-YOE depth + examples  |  Sanket Kolhe"

CONTENT = [
    {
        "phase": "FastAPI Phase 1 - Core",
        "topics": [
            {
                "title": "F1.1  What is FastAPI and Why Is It Fast",
                "what": "FastAPI is a modern async-first Python web framework built on Starlette (ASGI) and Pydantic (validation), driven entirely by type hints.",
                "points": [
                    "Two engines: Starlette handles async HTTP/routing; Pydantic handles data validation and serialization - FastAPI glues them with type hints.",
                    "\"Fast\" has two meanings: runtime speed (async event loop handles thousands of concurrent I/O-bound requests per worker) and developer speed (validation + docs generated from the same type hints).",
                    "Declare def f(item_id: int) - conversion, validation and the OpenAPI docs entry all come from that one hint. No separate schema, no manual casting.",
                    "Auto docs at /docs (Swagger UI) and /redoc - always in sync with the code because they come from the code.",
                    "Runs on uvicorn (ASGI server). Async is optional per endpoint - plain def works too.",
                    "Compared with Django: no ORM/admin/migrations built in - we bring SQLAlchemy/Alembic; FastAPI is the API layer only.",
                    "My use: serving AI/RAG endpoints and internal APIs where async fan-out to models/DBs matters.",
                ],
                "example": "from fastapi import FastAPI\napp = FastAPI()\n\n@app.get(\"/items/{item_id}\")\nasync def read_item(item_id: int):\n    return {\"item_id\": item_id}\n# /docs -> automatic Swagger UI",
                "answer": "FastAPI is an ASGI framework combining Starlette for async HTTP and Pydantic for validation, all driven by type hints - one annotation gives parsing, validation and Swagger docs. It is fast at runtime for I/O-heavy concurrency and fast to develop, but brings no ORM or admin - it is the API layer, which is why I use it for AI-serving endpoints.",
            },
            {
                "title": "F1.2  Path and Query Parameters",
                "what": "Function parameters become path or query parameters automatically - typed, validated and documented from the signature.",
                "points": [
                    "In the route path -> path parameter: /items/{item_id} with item_id: int. Not in the path -> query parameter: ?limit=10.",
                    "Types validate for free: item_id: int rejects /items/abc with a clear 422 error - no manual parsing.",
                    "Defaults make query params optional (limit: int = 10); Optional[str] = None for truly optional ones.",
                    "Constraints via Path() and Query(): Query(default=10, ge=1, le=100) - range rules, min_length, regex patterns.",
                    "bool query params accept true/false/1/0 automatically; list[int] = Query() accepts repeated params (?id=1&id=2).",
                    "Everything lands in the OpenAPI docs with types, defaults and constraints visible.",
                ],
                "example": "@app.get(\"/products\")\nasync def list_products(\n    q: str | None = None,\n    limit: int = Query(10, ge=1, le=100),\n    in_stock: bool = True,\n):\n    ...\n# /products?q=shirt&limit=20&in_stock=true",
                "answer": "Path variables come from the route ({item_id}) and everything else in the signature becomes a query parameter - typed, defaulted and validated automatically, with Query/Path adding constraints like ge/le or regex. Bad input gets a structured 422 without any code from me, and the docs show it all.",
            },
            {
                "title": "F1.3  Pydantic Models - Request Body and Validation",
                "what": "A Pydantic BaseModel declares the request body's shape; FastAPI parses, validates and types the JSON into a real object.",
                "points": [
                    "class OrderIn(BaseModel): amount: Decimal; note: str | None = None - a typed parameter of that model becomes the request body.",
                    "Validation is automatic and recursive: wrong types, missing fields, nested models, lists - all checked, failures return 422 with per-field error paths.",
                    "Field(gt=0, max_length=100) adds constraints; @field_validator writes custom rules (Pydantic v2 style; v1 used @validator - version awareness scores points).",
                    "Nested models compose naturally: an Order containing a list[Item].",
                    "model_dump() gives a dict (v2; dict() in v1); models also serialize back to JSON for responses.",
                    "Separate models per direction is the discipline: OrderIn (no id) vs OrderOut (id, created_at) - never expose internal fields by reusing one model everywhere.",
                    "Pydantic v2's core is compiled Rust - validation is genuinely fast.",
                ],
                "example": "class OrderIn(BaseModel):\n    amount: Decimal = Field(gt=0)\n    items: list[int]\n\n@app.post(\"/orders\")\nasync def create(order: OrderIn):\n    # order is a validated object\n    return {\"total\": order.amount}",
                "answer": "A BaseModel parameter becomes the validated request body - types, Field constraints and custom validators run automatically, failing with structured 422s. I keep separate input and output models so internal fields never leak, and in Pydantic v2 validation runs on a Rust core with model_dump replacing dict().",
            },
            {
                "title": "F1.4  response_model and Status Codes",
                "what": "response_model declares the output schema - filtering, validating and documenting the response - and status_code sets the success code.",
                "points": [
                    "@app.post(..., response_model=OrderOut): the return value is filtered to OrderOut's fields - extra/internal fields (password hashes, flags) are stripped, not leaked.",
                    "This is the output-security tool: return the ORM object; the model decides what leaves.",
                    "status_code=201 for creation, 204 for delete-no-content; the client sees it in docs too.",
                    "response_model_exclude_unset / exclude_none tune partial responses.",
                    "Returning a different shape than declared raises a server-side validation error - contract enforced both ways.",
                    "Union response models + responses={404: {...}} document error shapes in OpenAPI.",
                ],
                "example": "class OrderOut(BaseModel):\n    id: int\n    amount: Decimal\n    model_config = ConfigDict(\n        from_attributes=True)  # ORM mode\n\n@app.post(\"/orders\", response_model=OrderOut,\n          status_code=201)\nasync def create(order: OrderIn):\n    return save_order(order)  # extra fields stripped",
                "answer": "response_model is the declared output contract: the response is validated against it and any field not in the model is stripped, so internal data cannot leak even if I return a full ORM object. from_attributes enables ORM-object reading, and status_code plus documented error responses complete the OpenAPI contract.",
            },
            {
                "title": "F1.5  Dependency Injection - Depends()",
                "what": "Depends() lets endpoints declare what they need - DB session, current user, pagination - and FastAPI builds and injects it per request.",
                "points": [
                    "A dependency is just a callable; def get_db(): yield session - the code after yield runs at request end (cleanup), like a context manager.",
                    "Endpoints declare db: Session = Depends(get_db) - no globals, no manual wiring.",
                    "Dependencies nest: get_current_user depends on the token dependency, endpoints depend on get_current_user - auth chains compose cleanly.",
                    "Same dependency twice in one request is cached (resolved once) by default.",
                    "Overridable in tests: app.dependency_overrides[get_db] = fake_db - the killer testing feature, no monkeypatching.",
                    "Router/app-level dependencies apply checks to whole groups (e.g. every admin route requires the admin user).",
                    "This is the FastAPI-signature topic interviewers probe - the Django parallel is middleware + mixins, but DI is per-endpoint explicit and testable.",
                ],
                "example": "def get_db():\n    db = SessionLocal()\n    try:\n        yield db\n    finally:\n        db.close()\n\n@app.get(\"/orders\")\nasync def list_orders(\n    db: Session = Depends(get_db),\n    user: User = Depends(get_current_user)):\n    ...",
                "answer": "Depends() injects per-request resources - a yield dependency opens a DB session and closes it after the response, current-user dependencies chain off token dependencies for auth, results are cached within a request, and dependency_overrides swaps real dependencies for fakes in tests. It is FastAPI's core pattern: explicit, composable, testable.",
            },
            {
                "title": "F1.6  async vs sync Endpoints",
                "what": "async def endpoints run on the event loop; plain def endpoints run in a threadpool - choosing wrong is the classic FastAPI performance bug.",
                "points": [
                    "async def + await: non-blocking I/O interleaves - one worker handles many concurrent requests waiting on DBs/APIs.",
                    "Plain def: FastAPI runs it in a threadpool automatically, so blocking code does not stall the loop - a safe default for sync libraries.",
                    "THE bug: async def containing a blocking call (requests, time.sleep, sync DB driver) - the whole event loop freezes; every request waits. Symptom: mysterious latency spikes under load.",
                    "Rules: async work uses async libraries (httpx, asyncpg, SQLAlchemy async); stuck with sync libraries -> use plain def and let the threadpool absorb it.",
                    "asyncio.gather inside an endpoint fans out to multiple services concurrently - where async genuinely shines.",
                    "CPU-bound work helps neither model - offload to a worker/process pool.",
                ],
                "example": "# WRONG - blocks the loop:\n@app.get(\"/bad\")\nasync def bad():\n    r = requests.get(URL)      # blocking!\n# RIGHT:\n@app.get(\"/good\")\nasync def good():\n    async with httpx.AsyncClient() as c:\n        r1, r2 = await asyncio.gather(\n            c.get(URL1), c.get(URL2))",
                "answer": "async def runs on the event loop for non-blocking concurrency; plain def is auto-routed to a threadpool so sync code stays safe. The classic bug is blocking calls inside async def - requests or a sync driver freezes every request on that worker. My rule: async with async libraries like httpx, plain def with sync ones, gather for fan-out, and CPU work goes to workers.",
            },
            {
                "title": "F1.7  Error Handling",
                "what": "HTTPException returns structured error responses; custom exception handlers centralize how errors become JSON.",
                "points": [
                    "raise HTTPException(status_code=404, detail=\"Order not found\") - returns {\"detail\": ...} with the status; headers= can add e.g. WWW-Authenticate.",
                    "Validation failures return 422 automatically with per-field error locations - clients get machine-readable problems.",
                    "@app.exception_handler(OrderNotFound) maps domain exceptions to responses - services raise business errors, one handler formats them; endpoints stay clean.",
                    "Overriding RequestValidationError's handler customizes the 422 shape (matching a company error contract).",
                    "Unhandled exceptions become 500 - never leak internals in the message; log them (Sentry) instead.",
                    "Pattern: business logic raises domain exceptions; only the edge (handlers) knows about HTTP.",
                ],
                "example": "class OrderNotFound(Exception): ...\n\n@app.exception_handler(OrderNotFound)\nasync def handle_onf(request, exc):\n    return JSONResponse(status_code=404,\n        content={\"error\": \"order_not_found\"})\n\n# service code just raises OrderNotFound",
                "answer": "HTTPException covers direct cases, validation errors return structured 422s for free, and custom exception handlers map domain exceptions to HTTP responses centrally - so business code raises OrderNotFound and only the handler layer speaks HTTP. Unexpected errors stay generic 500s with details going to logging, never to the client.",
            },
        ],
    },
    {
        "phase": "FastAPI Phase 2 - Production",
        "topics": [
            {
                "title": "F2.1  Routers and Project Structure",
                "what": "APIRouter splits endpoints into modules per feature; the app include_router()s them - FastAPI's version of Django apps.",
                "points": [
                    "APIRouter(prefix=\"/orders\", tags=[\"orders\"]) - endpoints defined on the router; tags group them in Swagger.",
                    "app.include_router(orders.router) mounts it; a global /api/v1 prefix at include time gives versioning.",
                    "Typical layout: app/main.py (app + includes), routers/ (endpoints), schemas/ (Pydantic), models/ (SQLAlchemy), services/ (business logic), dependencies.py, core/config.py.",
                    "Keep endpoints thin: parse -> call service -> shape response. Business logic lives in services, testable without HTTP.",
                    "Router-level dependencies apply auth to a whole feature: APIRouter(dependencies=[Depends(admin_only)]).",
                    "Settings via pydantic-settings BaseSettings - env vars parsed and validated like any model.",
                ],
                "example": "# routers/orders.py\nrouter = APIRouter(prefix=\"/orders\",\n                   tags=[\"orders\"])\n@router.get(\"/\")\nasync def list_orders(...): ...\n# main.py\napp.include_router(orders.router,\n                   prefix=\"/api/v1\")",
                "answer": "APIRouter modularizes endpoints per feature with shared prefixes, tags and router-level auth dependencies, mounted via include_router with an /api/v1 prefix for versioning. I keep endpoints thin over a services layer, schemas and models in their own modules, and configuration in a validated pydantic-settings class.",
            },
            {
                "title": "F2.2  Middleware and CORS",
                "what": "Middleware wraps every request/response; CORSMiddleware is the one every SPA-backed API must configure.",
                "points": [
                    "@app.middleware(\"http\") or add_middleware() - code before call_next sees the request, after it the response (timing, request-id, logging).",
                    "CORS: browsers block cross-origin JS calls unless the server sends Access-Control-* headers; preflight OPTIONS requests come first for non-simple requests.",
                    "CORSMiddleware(allow_origins=[...], allow_methods, allow_headers, allow_credentials) - the fix for \"works in Postman, fails in browser\".",
                    "allow_origins=[\"*\"] cannot combine with allow_credentials=True - browsers reject it; list real origins in production.",
                    "Order matters here too - CORS middleware must sit early enough to decorate even error responses.",
                    "Heavier concerns (rate limiting, auth at the edge) often live in the gateway/nginx rather than app middleware.",
                ],
                "example": "app.add_middleware(\n    CORSMiddleware,\n    allow_origins=[\"https://shop.example.com\"],\n    allow_credentials=True,\n    allow_methods=[\"*\"],\n    allow_headers=[\"*\"],\n)",
                "answer": "Middleware wraps all requests for cross-cutting work like timing and request IDs. CORS is the browser's cross-origin gate - CORSMiddleware answers preflights and sets the allow headers; wildcard origins don't combine with credentials, so production lists exact origins. It is the standard fix for APIs that work in Postman but fail from the React app.",
            },
            {
                "title": "F2.3  Authentication - OAuth2 Password Flow + JWT",
                "what": "The standard FastAPI auth: a /token endpoint checks credentials and issues a JWT; a dependency validates the Bearer token on every protected route.",
                "points": [
                    "OAuth2PasswordBearer(tokenUrl=\"token\") extracts the Authorization: Bearer header and powers the Swagger login button.",
                    "/token endpoint: verify password (passlib/bcrypt hashes - never plain), then jwt.encode({\"sub\": username, \"exp\": ...}, SECRET, \"HS256\").",
                    "get_current_user dependency: decode + verify signature and expiry, load the user, raise 401 with WWW-Authenticate on failure.",
                    "Protected endpoints just declare user: User = Depends(get_current_user) - auth is a dependency, not a middleware, so per-route control is natural.",
                    "Same JWT trade-offs as Django notes: short expiry + refresh, revocation needs state, claims are readable - HTTPS always.",
                    "Role checks nest: require_admin depends on get_current_user and raises 403 - then routers include it wholesale.",
                ],
                "example": "oauth2 = OAuth2PasswordBearer(tokenUrl=\"token\")\n\nasync def get_current_user(\n        token: str = Depends(oauth2)):\n    try:\n        payload = jwt.decode(token, SECRET,\n                             algorithms=[\"HS256\"])\n    except JWTError:\n        raise HTTPException(401)\n    return await load_user(payload[\"sub\"])",
                "answer": "The pattern is OAuth2 password flow: /token verifies bcrypt-hashed credentials and returns a signed JWT with sub and exp; OAuth2PasswordBearer pulls the Bearer token and a get_current_user dependency decodes, verifies and loads the user, raising 401 on failure. Role checks are just nested dependencies, and the usual JWT caveats - short expiry, refresh, revocation statefulness - apply.",
            },
            {
                "title": "F2.4  Database - SQLAlchemy Session Pattern",
                "what": "FastAPI has no ORM; the standard stack is SQLAlchemy + Alembic migrations, with a session-per-request dependency.",
                "points": [
                    "SQLAlchemy: engine (pool) -> SessionLocal factory -> per-request session from a yield dependency that always closes it.",
                    "Endpoints/services receive db: Session = Depends(get_db) - the FastAPI equivalent of Django's request-scoped DB handling.",
                    "Alembic = makemigrations/migrate equivalent: autogenerate diffs, upgrade head applies - versioned in git the same way.",
                    "Pydantic from_attributes (ORM mode) converts SQLAlchemy objects to response models.",
                    "Fully async option: create_async_engine + AsyncSession + await db.execute(select(...)) - pairs with asyncpg; sync psycopg2 sessions in async def endpoints are the classic blocking bug again.",
                    "The 2.0-style select() API replaces legacy query() - worth naming in interviews.",
                    "Commit strategy: service commits, or a request-scoped commit/rollback in the dependency - pick one, consistently.",
                ],
                "example": "engine = create_engine(DB_URL, pool_size=10)\nSessionLocal = sessionmaker(bind=engine)\n\ndef get_db():\n    db = SessionLocal()\n    try:\n        yield db\n        db.commit()\n    except Exception:\n        db.rollback(); raise\n    finally:\n        db.close()",
                "answer": "FastAPI pairs with SQLAlchemy: an engine with a connection pool, a session factory, and a yield dependency giving each request a session that commits or rolls back and always closes. Alembic plays the migrations role. For full async I use create_async_engine with asyncpg and 2.0-style select - never a sync driver inside async def, which would block the loop.",
            },
            {
                "title": "F2.5  BackgroundTasks vs Celery",
                "what": "BackgroundTasks runs work after the response in the same process - fine for small jobs; Celery remains the answer for real workloads.",
                "points": [
                    "background_tasks.add_task(fn, args) - response returns first, task runs after in the same worker.",
                    "Good for: fire-and-forget small work - notification email, audit log write, cache warm.",
                    "Limits: no retries, no persistence (process restart loses it), no separate scaling, shares the web worker's CPU/time.",
                    "Celery/RQ/arq when: retries and reliability matter, heavy jobs (PDFs, scraping, ML), scheduling, or dedicated worker scaling - same reasoning as the Django notes.",
                    "arq/dramatiq are async-native lighter alternatives in FastAPI projects.",
                    "Rule: would it hurt if this silently never ran? If yes - a real queue, not BackgroundTasks.",
                ],
                "example": "@app.post(\"/orders\")\nasync def create(order: OrderIn,\n        bg: BackgroundTasks):\n    saved = await save(order)\n    bg.add_task(send_email, saved.id)\n    return saved  # responds before email",
                "answer": "BackgroundTasks defers small fire-and-forget work until after the response but lives in the same process - no retries, no persistence, no independent scaling. My rule: if it must not be lost, it goes to a real queue - Celery, or async-native arq - with the web process only enqueueing.",
            },
            {
                "title": "F2.6  Testing - TestClient",
                "what": "TestClient calls the app in-process with the requests API; dependency_overrides swap real resources for fakes.",
                "points": [
                    "client = TestClient(app); client.post(\"/orders\", json={...}) - no server needed, assert status_code and .json().",
                    "app.dependency_overrides[get_db] = test_db - tests run on SQLite/memory or a fixture DB; override get_current_user to fake auth without token dances.",
                    "pytest fixtures build client + DB per test/session; httpx.AsyncClient(app=...) tests async endpoints natively.",
                    "Validation is already tested by FastAPI - focus tests on business logic, permission matrix (401/403/404) and contract shapes.",
                    "The DI design is what makes this clean - no monkeypatching, just override the dependency graph.",
                    "schemathesis/property tests can fuzz endpoints straight from the OpenAPI schema - bonus point.",
                ],
                "example": "def test_create_order(client):\n    app.dependency_overrides[get_current_user] = \\\n        lambda: fake_user\n    r = client.post(\"/api/v1/orders\",\n                    json={\"amount\": \"99.5\",\n                          \"items\": [1]})\n    assert r.status_code == 201\n    assert r.json()[\"amount\"] == \"99.5\"",
                "answer": "TestClient exercises the app in-process with a requests-style API, and dependency_overrides is the superpower - swap the DB session or current user for fakes without monkeypatching. I cover the permission matrix and business logic, use AsyncClient for async endpoints, and let the OpenAPI schema drive fuzz tests when time allows.",
            },
            {
                "title": "F2.7  Auto Docs and Deployment",
                "what": "OpenAPI docs generate themselves from the code; production runs uvicorn workers - usually under gunicorn - behind nginx.",
                "points": [
                    "/docs (Swagger UI) and /redoc render from the generated OpenAPI JSON - types, examples, auth button; always current because the code is the source.",
                    "Enrich docs with tags, summary/description, Field(examples=[...]), documented error responses; docs_url=None hides them on locked-down deployments.",
                    "The schema doubles as a contract: frontend teams generate typed clients from openapi.json.",
                    "Deploy: gunicorn -k uvicorn.workers.UvicornWorker -w 4 - gunicorn manages processes, each worker an async event loop. nginx/traefik in front for TLS and buffering; containerized in my projects (ECS/App Runner/k8s).",
                    "Worker count: CPU-bound formulas matter less - async workers multiply concurrency per process; measure.",
                    "Production checklist: settings from env, real CORS origins, structured logging with request IDs, /health endpoint, APM/Sentry.",
                ],
                "example": "gunicorn app.main:app \\\n  -k uvicorn.workers.UvicornWorker \\\n  -w 4 --bind 0.0.0.0:8000\n# docker: same line as CMD; nginx in front",
                "answer": "FastAPI generates Swagger and ReDoc from the code's types - always in sync, enrichable with tags and examples, and the OpenAPI JSON doubles as a client-generation contract. Production runs gunicorn managing uvicorn workers behind nginx, containerized with env-driven settings, health checks and monitoring - in my case on AWS ECS and App Runner.",
            },
        ],
    },
]
