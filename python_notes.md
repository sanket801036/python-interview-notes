# Python Interview Notes — Task Tracker

> Ye file **plan aur progress** ke liye hai. Actual notes Word file mein jayenge.
> Har topic complete hone par yahan status update hoga, taaki context na bhoole.

---

## Goal (kya banana hai)

Ek **Word document** jisme Python ke interview topics ki **sirf theory** ho —
simple English words mein, taaki yaad karke interviewer ko bola ja sake.

## Rules (har topic par lagu)

| Rule | Detail |
|---|---|
| Language | Simple English — chhote words, chhote sentences. No heavy jargon. |
| Content | **Sirf theory** abhi. Code examples baad mein alag phase mein. |
| Style | Har topic: 1-line definition → 3-5 point explanation → 1-line "interview answer" |
| Font size | **Small (9-10 pt)** — print nikalna hai, kam pages banein |
| Format | Word (.docx), headings + bullets, no big paragraphs |
| Audience | Sanket — 3 yrs exp, Python Full-Stack / AI Developer, switch planning |

## Files

| File | Kya hai |
|---|---|
| `Python_Interview_Theory.docx` | **Final Word file** — yahi print karna hai |
| `notes_content.py` | Saara text yahan hai. Naya phase yahin add hota hai. |
| `build_docx.py` | Content se Word file banata hai. Command: `python build_docx.py` |

> Word file **haath se edit mat karna** — `notes_content.py` badal ke script dobara
> chalao, warna agli baar changes overwrite ho jayenge.

Repo: https://github.com/sanket801036/python-interview-notes

---

## Topic List (jo cover karna hai)

### Phase 1 — Python Basics ✅ DONE
- [x] 1.1 Python kya hai — interpreted, dynamically typed, GIL ka zikr
- [x] 1.2 Python 2 vs Python 3 (short)
- [x] 1.3 Data types — int, float, str, bool, None
- [x] 1.4 Mutable vs Immutable
- [x] 1.5 Variables, memory, reference vs value
- [x] 1.6 Type casting / type conversion

### Phase 2 — Data Structures ✅ DONE
- [x] 2.1 List — kab use karein, kaise kaam karta hai
- [x] 2.2 Tuple — list se difference
- [x] 2.3 Set — uniqueness, hashing
- [x] 2.4 Dictionary — key-value, hashing, ordering
- [x] 2.5 String — immutability, common operations
- [x] 2.6 List vs Tuple vs Set vs Dict (comparison table)
- [x] 2.7 Shallow copy vs Deep copy

### Phase 3 — Functions ✅ DONE
- [x] 3.1 Function basics, return
- [x] 3.2 *args and **kwargs
- [x] 3.3 Default arguments — mutable default ka trap
- [x] 3.4 Scope — Local, Enclosing, Global, Built-in (LEGB)
- [x] 3.5 Lambda function
- [x] 3.6 map, filter, reduce
- [x] 3.7 Closure
- [x] 3.8 Decorator (bahut poocha jata hai)
- [x] 3.9 Recursion basics

### Phase 4 — OOP (Object Oriented Programming) ✅ DONE
- [x] 4.1 Class aur Object
- [x] 4.2 `__init__`, `self`
- [x] 4.3 Four pillars — Encapsulation, Abstraction, Inheritance, Polymorphism
- [x] 4.4 Types of inheritance + MRO (Method Resolution Order)
- [x] 4.5 Method overloading vs overriding
- [x] 4.6 instance method vs class method vs static method
- [x] 4.7 Dunder / magic methods (`__str__`, `__len__`, `__eq__`)
- [x] 4.8 `@property`, getters and setters
- [x] 4.9 Abstract class vs Interface
- [x] 4.10 Composition vs Inheritance

### Phase 5 — Advanced Python ✅ DONE
- [x] 5.1 Iterator vs Iterable
- [x] 5.2 Generator aur `yield` (memory benefit)
- [x] 5.3 List comprehension vs generator expression
- [x] 5.4 Context manager aur `with` statement
- [x] 5.5 Exception handling — try, except, else, finally
- [x] 5.6 Custom exceptions
- [x] 5.7 Garbage collection aur reference counting
- [x] 5.8 GIL (Global Interpreter Lock) — bahut poocha jata hai
- [x] 5.9 Multithreading vs Multiprocessing (kab kaunsa)
- [x] 5.10 async / await — asyncio basics
- [x] 5.11 Modules, packages, `__name__ == "__main__"`
- [x] 5.12 Virtual environment aur pip

### Phase 6 — Interview Favourites (mixed) ✅ DONE
- [x] 6.1 `is` vs `==`
- [x] 6.2 Memory management in Python
- [x] 6.3 Pass by value vs pass by reference
- [x] 6.4 Monkey patching
- [x] 6.5 `__new__` vs `__init__`
- [x] 6.6 Duck typing
- [x] 6.7 Python ke performance tips
- [x] 6.8 Common built-in functions (zip, enumerate, any, all, sorted)

---

## Progress Log

| Date | Kya hua |
|---|---|
| 2026-08-08 | Task file banayi. Topic list finalize kiya. |
| 2026-08-08 | **Phase 1 complete** (6 topics). Word file bani, GitHub repo bana ke push kiya. |
| 2026-08-08 | **Phase 2–6 complete.** 🎉 **PYTHON THEORY DONE — saare 52 topics Word file mein hain.** |
| 2026-08-09 | **SQL Phases 1–5 complete.** 🎉 **SQL DONE — 34 topics, har topic mein example query.** |
| 2026-08-10 | **Django Phases 1–5 complete.** 🎉 **DJANGO DONE — 34 topics, 3-YOE depth, examples ke saath.** |
| 2026-08-10 | **FastAPI Phases 1–2 complete.** 🎉 **FASTAPI DONE — 14 topics (compact).** |
| 2026-08-10 | **React Phases 1–3 complete.** 🎉 **REACT DONE — 21 topics + React Native/Expo.** Total ab: 5 docs, 155 topics. |

---

## Next Step

✅ Python theory poori (52/52). ➡️ Ab **SQL** chal raha hai (niche list).

---

# SQL Interview Notes

**Output:** `SQL_Interview_Theory.docx` · **Content:** `sql_content.py` · Same rules (simple English, small font) **+ har topic ke saath chhota example query** (Sanket ne 09 Aug ko bola).

### SQL Phase 1 — Basics ✅ DONE
- [x] S1.1 SQL kya hai, database, DBMS vs RDBMS
- [x] S1.2 SQL command types — DDL, DML, DQL, DCL, TCL
- [x] S1.3 Common data types
- [x] S1.4 Constraints — NOT NULL, UNIQUE, CHECK, DEFAULT
- [x] S1.5 Primary Key vs Foreign Key
- [x] S1.6 NULL — behavior, IS NULL, COALESCE

### SQL Phase 2 — Core Queries ✅ DONE
- [x] S2.1 SELECT, WHERE, operators (IN, BETWEEN, LIKE)
- [x] S2.2 DISTINCT, ORDER BY, LIMIT/OFFSET
- [x] S2.3 Aggregate functions — COUNT, SUM, AVG, MIN, MAX
- [x] S2.4 GROUP BY aur HAVING
- [x] S2.5 String & date functions (common)
- [x] S2.6 CASE expression

### SQL Phase 3 — Joins & Subqueries ✅ DONE
- [x] S3.1 JOIN kya hai + INNER JOIN
- [x] S3.2 LEFT, RIGHT, FULL OUTER JOIN
- [x] S3.3 CROSS JOIN aur SELF JOIN
- [x] S3.4 UNION vs UNION ALL
- [x] S3.5 Subqueries — single row, multi row, correlated
- [x] S3.6 EXISTS vs IN

### SQL Phase 4 — Advanced ✅ DONE
- [x] S4.1 Indexes — kaise kaam karte hain, kab lagayein
- [x] S4.2 Views
- [x] S4.3 Stored procedures aur triggers
- [x] S4.4 Transactions aur ACID
- [x] S4.5 Isolation levels aur common problems
- [x] S4.6 Window functions — ROW_NUMBER, RANK, PARTITION BY
- [x] S4.7 CTE (WITH clause)
- [x] S4.8 Normalization — 1NF, 2NF, 3NF + denormalization

# AWS / Cloud Interview Notes

**Output:** `AWS_Interview_Theory.docx` · **Content:** `aws_content.py` ·
Resume-aligned (ECS, ECR, App Runner, IAM, ALB resume mein hain — deep cover).
3-YOE depth + examples (CLI/config).

### AWS Phase 1 — Core Concepts ✅ DONE
- [x] A1.1 AWS kya hai — regions, AZs, shared responsibility
- [x] A1.2 IAM — users, roles, policies (resume item)
- [x] A1.3 EC2 — instances, AMI, security groups
- [x] A1.4 S3 — buckets, storage classes, presigned URLs
- [x] A1.5 VPC basics — subnets, SG vs NACL, IGW/NAT
- [x] A1.6 Pricing model — on-demand, reserved, spot, free tier

### AWS Phase 2 — Compute & Containers (resume core) ✅ DONE
- [x] A2.1 Docker recap — image, container, Dockerfile (interview angle)
- [x] A2.2 ECR — registry, push flow (resume item)
- [x] A2.3 ECS — cluster, task definition, service (resume item)
- [x] A2.4 Fargate vs EC2 launch type
- [x] A2.5 App Runner — kab sahi (resume item)
- [x] A2.6 ALB + Auto Scaling (resume item)
- [x] A2.7 Lambda — serverless, kab use, limits

### AWS Phase 3 — Data & Messaging
- [ ] A3.1 RDS — managed Postgres/MySQL, Multi-AZ vs read replica
- [ ] A3.2 ElastiCache — Redis on AWS
- [ ] A3.3 DynamoDB — kab NoSQL (short)
- [ ] A3.4 SQS/SNS — queues aur pub-sub
- [ ] A3.5 Route 53 + CloudFront — DNS aur CDN

### AWS Phase 4 — DevOps & Production
- [ ] A4.1 CloudWatch — logs, metrics, alarms
- [ ] A4.2 CI/CD to AWS — Jenkins pipeline flow (resume item)
- [ ] A4.3 Secrets management — SSM, Secrets Manager
- [ ] A4.4 Security best practices — least privilege, no root keys
- [ ] A4.5 Cost optimization — 3-YOE level answers
- [ ] A4.6 Architecture walkthrough — RAG chatbot on AWS (resume story)

# React Interview Notes

**Output:** `React_Interview_Theory.docx` · **Content:** `react_content.py` ·
3-YOE depth, JSX examples. React Native/Expo touch bhi (Fabric Dispatch app ke liye).

### React Phase 1 — Fundamentals ✅ DONE
- [x] R1.1 React kya hai — Virtual DOM, JSX
- [x] R1.2 Components aur Props
- [x] R1.3 State — useState, immutability
- [x] R1.4 Rendering, reconciliation, keys
- [x] R1.5 Conditional rendering aur lists
- [x] R1.6 Forms — controlled vs uncontrolled
- [x] R1.7 useEffect — lifecycle ki jagah

### React Phase 2 — Hooks & State Management ✅ DONE
- [x] R2.1 useEffect deep — dependencies, cleanup, common bugs
- [x] R2.2 useMemo, useCallback, React.memo
- [x] R2.3 useRef — DOM access aur mutable values
- [x] R2.4 Custom hooks
- [x] R2.5 Context API — props drilling ka solution
- [x] R2.6 Redux / Zustand — global state kab chahiye
- [x] R2.7 Lifting state up, composition patterns

### React Phase 3 — Ecosystem & Production ✅ DONE
- [x] R3.1 React Router
- [x] R3.2 API calls — fetching patterns, React Query
- [x] R3.3 Performance optimization checklist
- [x] R3.4 Code splitting — React.lazy, Suspense
- [x] R3.5 Error boundaries
- [x] R3.6 React 18 — concurrent features, batching
- [x] R3.7 React Native / Expo — web se difference

# FastAPI Interview Notes (compact)

**Output:** `FastAPI_Interview_Theory.docx` · **Content:** `fastapi_content.py` ·
Compact — 2 phases, FastAPI-specific topics only (Django-overlap skip). Baad mein React.

### FastAPI Phase 1 — Core ✅ DONE
- [x] F1.1 FastAPI kya hai, kyun fast, Starlette + Pydantic
- [x] F1.2 Path & query parameters — type hints se validation
- [x] F1.3 Pydantic models — request body, validation
- [x] F1.4 response_model aur status codes
- [x] F1.5 Dependency Injection — Depends()
- [x] F1.6 async vs sync endpoints — kab kya
- [x] F1.7 Error handling — HTTPException, custom handlers

### FastAPI Phase 2 — Production ✅ DONE
- [x] F2.1 Routers — project structure
- [x] F2.2 Middleware aur CORS
- [x] F2.3 Auth — OAuth2 password flow + JWT
- [x] F2.4 Database — SQLAlchemy session pattern
- [x] F2.5 BackgroundTasks vs Celery
- [x] F2.6 Testing — TestClient
- [x] F2.7 Auto docs (Swagger) aur deployment (uvicorn workers)

# Django Interview Notes

**Output:** `Django_Interview_Theory.docx` · **Content:** `django_content.py` ·
Level: **3-year experience** — surface definition nahi, depth wale answers
(ORM internals, N+1, DRF, deployment). Har topic mein example. (10 Aug ko shuru.)

### Django Phase 1 — Core Architecture ✅ DONE
- [x] D1.1 Django kya hai, MTV pattern, batteries-included
- [x] D1.2 Request/response cycle — WSGI se view tak
- [x] D1.3 Project vs app, settings ka structure
- [x] D1.4 URL routing, path converters, reverse()
- [x] D1.5 FBV vs CBV — kab kaunsa
- [x] D1.6 Templates (short — API dev ke liye kaam bhar)

### Django Phase 2 — Models & ORM (sabse important) ✅ DONE
- [x] D2.1 Models aur migrations ka flow
- [x] D2.2 QuerySet — lazy evaluation, caching
- [x] D2.3 select_related vs prefetch_related — N+1 problem
- [x] D2.4 F objects, Q objects, aggregation
- [x] D2.5 Relationships — FK, OneToOne, ManyToMany, related_name
- [x] D2.6 Model inheritance — abstract, multi-table, proxy
- [x] D2.7 Transactions — atomic, select_for_update
- [x] D2.8 Custom managers aur querysets

### Django Phase 3 — Middleware, Auth, Signals, Caching ✅ DONE
- [x] D3.1 Middleware — kaise kaam karta hai, custom likhna
- [x] D3.2 Signals — kab use, kab avoid
- [x] D3.3 Authentication — sessions, custom user model
- [x] D3.4 Permissions aur groups
- [x] D3.5 Security features — CSRF, XSS, SQL injection protection
- [x] D3.6 Caching — levels aur Redis

### Django Phase 4 — Django REST Framework ✅ DONE
- [x] D4.1 DRF kya hai, kyun
- [x] D4.2 Serializers — validation, nested, SerializerMethodField
- [x] D4.3 APIView vs generics vs ViewSet + routers
- [x] D4.4 Authentication — Token, JWT, session
- [x] D4.5 Permissions aur throttling
- [x] D4.6 Pagination, filtering, searching
- [x] D4.7 DRF testing basics

### Django Phase 5 — Production & Interview Favourites ✅ DONE
- [x] D5.1 Django vs Flask vs FastAPI
- [x] D5.2 N+1 detect karna — debug toolbar, query counting
- [x] D5.3 Static vs media files, production serving
- [x] D5.4 Deployment — gunicorn, nginx, ASGI
- [x] D5.5 Performance tips — experienced-level checklist
- [x] D5.6 Celery — background tasks
- [x] D5.7 Django async views — kab helpful, limits

### SQL Phase 5 — Interview Favourites ✅ DONE
- [x] S5.1 DELETE vs TRUNCATE vs DROP
- [x] S5.2 WHERE vs HAVING
- [x] S5.3 Primary key vs Unique key
- [x] S5.4 CHAR vs VARCHAR vs TEXT
- [x] S5.5 Nth highest salary — approaches (theory)
- [x] S5.6 SQL injection aur bachav
- [x] S5.7 Query optimization tips
- [x] S5.8 OLTP vs OLAP

---

## Note

`python-docx` library install nahi ho paayi (permission block), isliye `build_docx.py`
Word file ko seedha OOXML (zipfile + XML) se banata hai. Ye standard format hai,
Word / Google Docs / WPS sabme khulega. Is machine par Word installed nahi hai
isliye render check nahi ho paaya — Sanket ek baar khol ke dekh le.
