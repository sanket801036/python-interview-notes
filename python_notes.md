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

### Phase 4 — OOP (Object Oriented Programming)
- [ ] 4.1 Class aur Object
- [ ] 4.2 `__init__`, `self`
- [ ] 4.3 Four pillars — Encapsulation, Abstraction, Inheritance, Polymorphism
- [ ] 4.4 Types of inheritance + MRO (Method Resolution Order)
- [ ] 4.5 Method overloading vs overriding
- [ ] 4.6 instance method vs class method vs static method
- [ ] 4.7 Dunder / magic methods (`__str__`, `__len__`, `__eq__`)
- [ ] 4.8 `@property`, getters and setters
- [ ] 4.9 Abstract class vs Interface
- [ ] 4.10 Composition vs Inheritance

### Phase 5 — Advanced Python
- [ ] 5.1 Iterator vs Iterable
- [ ] 5.2 Generator aur `yield` (memory benefit)
- [ ] 5.3 List comprehension vs generator expression
- [ ] 5.4 Context manager aur `with` statement
- [ ] 5.5 Exception handling — try, except, else, finally
- [ ] 5.6 Custom exceptions
- [ ] 5.7 Garbage collection aur reference counting
- [ ] 5.8 GIL (Global Interpreter Lock) — bahut poocha jata hai
- [ ] 5.9 Multithreading vs Multiprocessing (kab kaunsa)
- [ ] 5.10 async / await — asyncio basics
- [ ] 5.11 Modules, packages, `__name__ == "__main__"`
- [ ] 5.12 Virtual environment aur pip

### Phase 6 — Interview Favourites (mixed)
- [ ] 6.1 `is` vs `==`
- [ ] 6.2 Memory management in Python
- [ ] 6.3 Pass by value vs pass by reference
- [ ] 6.4 Monkey patching
- [ ] 6.5 `__new__` vs `__init__`
- [ ] 6.6 Duck typing
- [ ] 6.7 Python ke performance tips
- [ ] 6.8 Common built-in functions (zip, enumerate, any, all, sorted)

---

## Progress Log

| Date | Kya hua |
|---|---|
| 2026-08-08 | Task file banayi. Topic list finalize kiya. |
| 2026-08-08 | **Phase 1 complete** (6 topics). Word file bani, GitHub repo bana ke push kiya. |

---

## Next Step

➡️ **Phase 2 — Data Structures** (7 topics: List, Tuple, Set, Dict, String,
comparison table, shallow vs deep copy)

---

## Note

`python-docx` library install nahi ho paayi (permission block), isliye `build_docx.py`
Word file ko seedha OOXML (zipfile + XML) se banata hai. Ye standard format hai,
Word / Google Docs / WPS sabme khulega. Is machine par Word installed nahi hai
isliye render check nahi ho paaya — Sanket ek baar khol ke dekh le.
