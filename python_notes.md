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

### SQL Phase 4 — Advanced
- [ ] S4.1 Indexes — kaise kaam karte hain, kab lagayein
- [ ] S4.2 Views
- [ ] S4.3 Stored procedures aur triggers
- [ ] S4.4 Transactions aur ACID
- [ ] S4.5 Isolation levels aur common problems
- [ ] S4.6 Window functions — ROW_NUMBER, RANK, PARTITION BY
- [ ] S4.7 CTE (WITH clause)
- [ ] S4.8 Normalization — 1NF, 2NF, 3NF + denormalization

### SQL Phase 5 — Interview Favourites
- [ ] S5.1 DELETE vs TRUNCATE vs DROP
- [ ] S5.2 WHERE vs HAVING
- [ ] S5.3 Primary key vs Unique key
- [ ] S5.4 CHAR vs VARCHAR vs TEXT
- [ ] S5.5 Nth highest salary — approaches (theory)
- [ ] S5.6 SQL injection aur bachav
- [ ] S5.7 Query optimization tips
- [ ] S5.8 OLTP vs OLAP

---

## Note

`python-docx` library install nahi ho paayi (permission block), isliye `build_docx.py`
Word file ko seedha OOXML (zipfile + XML) se banata hai. Ye standard format hai,
Word / Google Docs / WPS sabme khulega. Is machine par Word installed nahi hai
isliye render check nahi ho paaya — Sanket ek baar khol ke dekh le.
