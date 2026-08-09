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
]
