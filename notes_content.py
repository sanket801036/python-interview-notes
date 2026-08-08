"""Content for Python_Interview_Theory.docx.

Add one phase at a time, then re-run build_docx.py.
Format for every topic:  what (1 line) -> points (3-6 bullets) -> answer (1 line).
Keep the English simple: short words, short sentences.
"""

DOC_TITLE = "Python Interview Theory Notes"
DOC_SUBTITLE = "Simple English  |  Theory only  |  Sanket Kolhe"

CONTENT = [
    {
        "phase": "Phase 1 - Python Basics",
        "topics": [
            {
                "title": "1.1  What is Python?",
                "what": "Python is a high-level, interpreted programming language that is easy to read and write.",
                "points": [
                    "High-level: we do not manage memory or hardware ourselves. Python does it for us.",
                    "Interpreted: the code runs line by line. There is no separate compile step. This makes testing fast, but it runs slower than C or Java.",
                    "Dynamically typed: we do not write the type. x = 5 and then x = \"hi\" is allowed. The type is checked when the code runs.",
                    "Multi-paradigm: it supports object oriented code (classes), and also functional style (functions used as values).",
                    "Very large library support: web (Django, Flask, FastAPI), AI (PyTorch, LangChain), data (Pandas, NumPy).",
                    "Cross platform: the same code runs on Windows, Linux and Mac.",
                    "One weak point: the GIL (Global Interpreter Lock). Only one thread can run Python code at a time, so heavy CPU work does not get faster with threads.",
                ],
                "answer": "Python is a high-level, interpreted, dynamically typed language. It is quick to write, has a huge library ecosystem, and is used for web, automation and AI. Its main limit is the GIL, which blocks true multithreading for CPU-heavy work.",
            },
            {
                "title": "1.2  Python 2 vs Python 3",
                "what": "Python 2 is old and no longer supported. All new work today is done in Python 3.",
                "points": [
                    "Support for Python 2 ended in January 2020. It gets no security fixes now.",
                    "print: in Python 2 it was a statement (print \"hi\"). In Python 3 it is a function (print(\"hi\")).",
                    "Division: in Python 2, 5/2 gave 2. In Python 3, 5/2 gives 2.5. Use // when we want the floor value.",
                    "Strings: in Python 2, str was bytes and unicode was separate. In Python 3, str is Unicode by default and bytes is a separate type.",
                    "range: in Python 2, range() built a full list in memory. In Python 3, range() is lazy, so it saves memory.",
                    "Errors: Python 3 uses \"except Error as e\", which is clearer than the old comma style.",
                ],
                "answer": "Python 2 reached end of life in 2020. The main changes in Python 3 are print as a function, true division, Unicode strings by default, and a lazy range that saves memory.",
            },
            {
                "title": "1.3  Data Types",
                "what": "A data type tells us what kind of value a variable holds and what we can do with it.",
                "points": [
                    "Numbers: int (whole number, no size limit in Python), float (decimal), complex (real + imaginary).",
                    "Text: str, used for any text. It is always Unicode in Python 3.",
                    "Boolean: bool, only True or False. It is a subclass of int, so True == 1 and False == 0.",
                    "Sequences: list (ordered, changeable), tuple (ordered, fixed), range (lazy number sequence).",
                    "Sets: set (unique items, unordered) and frozenset (a set that cannot be changed).",
                    "Mapping: dict, which stores key and value pairs. Since Python 3.7 it keeps insertion order.",
                    "Binary: bytes and bytearray, used for files, images and network data.",
                    "None: the NoneType value. It means \"no value here\", and it is not the same as 0 or \"\".",
                    "Everything in Python is an object, so even an integer or a function has methods.",
                    "type() tells us the exact type. isinstance() is safer because it also accepts child classes.",
                ],
                "answer": "Python has numbers, strings, booleans, lists, tuples, sets, dicts, bytes and None. Everything is an object, so even an integer has methods. I use isinstance() rather than type() for checks, because it also works for subclasses.",
            },
            {
                "title": "1.4  Mutable vs Immutable",
                "what": "Mutable means the object can be changed after it is created. Immutable means it cannot be changed.",
                "points": [
                    "Immutable types: int, float, str, tuple, bool, bytes, frozenset.",
                    "Mutable types: list, dict, set, bytearray, and normally our own class objects.",
                    "When we \"change\" an immutable object, Python actually makes a new object in memory. The old id is left behind.",
                    "A mutable object sent to a function can be changed inside that function, and the caller sees the change. An immutable one cannot.",
                    "Only immutable (hashable) objects can be used as dictionary keys or set items. A tuple can be a key, a list cannot.",
                    "Common bug: a mutable default argument, like def f(items=[]). That one list is shared by every call. The fix is to use None as the default and create a new list inside.",
                ],
                "answer": "Immutable objects like str and tuple cannot change after they are created, so any edit makes a new object. Mutable ones like list and dict change in place. This matters for dictionary keys, and it explains the classic mutable default argument bug.",
            },
            {
                "title": "1.5  Variables and Memory",
                "what": "In Python a variable is not a box that holds a value. It is a name that points to an object in memory.",
                "points": [
                    "Assignment binds a name to an object. It does not copy the data.",
                    "a = [1, 2] and then b = a makes both names point to the same list. Changing b also changes a.",
                    "id() gives the memory address of an object. \"is\" compares the address, \"==\" compares the value.",
                    "Reference counting: Python counts how many names point to an object. When the count drops to zero, the memory is freed at once.",
                    "A garbage collector also runs to clean up reference cycles, which counting alone cannot free.",
                    "Interning: small integers (-5 to 256) and short strings are cached and reused by Python to save memory and time.",
                    "To get a real copy we use copy.copy() for a shallow copy or copy.deepcopy() for a full copy.",
                ],
                "answer": "Variables in Python are names bound to objects, not memory boxes. Assignment copies the reference, not the data. Python frees memory with reference counting, plus a garbage collector for cycles.",
            },
            {
                "title": "1.6  Type Casting (Type Conversion)",
                "what": "Type casting means changing a value from one data type into another.",
                "points": [
                    "Implicit casting is done by Python itself. For example 5 + 2.0 gives 7.0, because the int is promoted to float. No data is lost.",
                    "Explicit casting is done by us, using int(), float(), str(), list(), tuple(), set(), dict() or bool().",
                    "int(\"10\") works, but int(\"abc\") raises a ValueError. So we wrap user input or file data in try/except.",
                    "int(3.9) gives 3. It cuts the decimal part, it does not round. Use round() when we want rounding.",
                    "Falsy values are 0, 0.0, \"\", [], {}, set() and None. bool() turns them into False. Everything else becomes True.",
                    "Casting between collections is common: list(my_set) to make it ordered, or set(my_list) to remove duplicates.",
                ],
                "answer": "Implicit casting is done by Python, like int to float in mixed maths. Explicit casting is done by us with int(), str(), list() and so on. Bad conversions raise ValueError, so I always guard casts on outside data with try/except.",
            },
        ],
    },
    {
        "phase": "Phase 2 - Data Structures",
        "topics": [
            {
                "title": "2.1  List",
                "what": "A list is an ordered, changeable collection that can hold any type of items.",
                "points": [
                    "Ordered: items keep the position we gave them, and we can reach any item by index, like items[0].",
                    "Mutable: we can add, remove or change items after the list is made.",
                    "It can mix types: [1, \"two\", 3.0, [4]] is valid, though mixing is not a good habit.",
                    "Common methods: append (add at end), insert (add at position), extend (join another list), remove (by value), pop (by index, returns the item), sort, reverse.",
                    "Under the hood it is a dynamic array. Reading by index is O(1). append at the end is fast. insert or remove at the front is slow, O(n), because all items shift.",
                    "Slicing gives a new list: items[1:4], items[::-1] for reverse copy.",
                    "For heavy adding and removing at both ends, collections.deque is faster than a list.",
                ],
                "answer": "A list is Python's ordered, mutable collection, backed by a dynamic array. Index access and append are fast, but inserting at the front is O(n). I use it when order matters and the data will change.",
            },
            {
                "title": "2.2  Tuple",
                "what": "A tuple is an ordered collection like a list, but it cannot be changed after creation.",
                "points": [
                    "Immutable: no append, no remove, no item assignment. Any \"change\" needs a new tuple.",
                    "Written with round brackets: (1, 2, 3). A single item tuple needs a comma: (5,).",
                    "Because it is immutable, a tuple can be a dictionary key or a set member. A list cannot.",
                    "It is a little faster and uses a little less memory than a list of the same items.",
                    "Great for fixed records, like a point (x, y) or a database row, where position has meaning.",
                    "Tuple unpacking is common: x, y = point, or a, b = b, a to swap values.",
                    "Note: if a tuple holds a list inside, that inner list can still change. The tuple only fixes which objects it holds, not their inner state.",
                ],
                "answer": "A tuple is an immutable ordered collection. It is hashable, so it can be a dict key, it is slightly faster than a list, and it is best for fixed data like coordinates or records. I use a list when data changes and a tuple when it should not.",
            },
            {
                "title": "2.3  Set",
                "what": "A set is an unordered collection of unique items.",
                "points": [
                    "Duplicates are removed automatically: set([1, 1, 2]) becomes {1, 2}.",
                    "Unordered: there is no index. We cannot ask for s[0].",
                    "Very fast membership test: \"x in my_set\" is O(1) on average, because a set uses a hash table. The same test on a list is O(n).",
                    "Set maths is built in: union (|), intersection (&), difference (-), symmetric difference (^).",
                    "Items must be hashable, so a list cannot go inside a set, but a tuple can.",
                    "frozenset is the immutable version, useful as a dict key.",
                    "Common uses: removing duplicates from a list, and fast \"already seen?\" checks.",
                ],
                "answer": "A set stores unique items in a hash table, so lookups and duplicate removal are O(1) on average. It has no order and no index. I use it for membership checks and set maths like union and intersection.",
            },
            {
                "title": "2.4  Dictionary",
                "what": "A dictionary stores data as key and value pairs, and finds a value by its key very fast.",
                "points": [
                    "Written as {\"name\": \"Sanket\", \"city\": \"Surat\"}. Lookup is d[\"name\"].",
                    "Keys must be unique and hashable (str, int, tuple). Values can be anything.",
                    "It is a hash table inside, so get, set and delete are O(1) on average.",
                    "Since Python 3.7, a dict keeps insertion order.",
                    "d[\"missing\"] raises KeyError. d.get(\"missing\", default) returns the default safely.",
                    "Useful methods: keys(), values(), items() for looping, update() to merge, pop() to remove.",
                    "defaultdict gives an automatic default value, Counter counts items - both from the collections module.",
                    "Dict comprehension: {k: v * 2 for k, v in d.items()}.",
                ],
                "answer": "A dict is a hash table of key-value pairs with O(1) average lookup. Keys must be hashable and unique, and since Python 3.7 insertion order is kept. I use get() to avoid KeyError, and defaultdict or Counter for counting patterns.",
            },
            {
                "title": "2.5  String",
                "what": "A string is an immutable sequence of Unicode characters.",
                "points": [
                    "Immutable: s[0] = \"x\" is an error. Every edit, like replace or upper, returns a new string.",
                    "It is a sequence, so indexing and slicing work: s[0], s[-1], s[2:5], s[::-1] to reverse.",
                    "Common methods: strip, split, join, replace, upper, lower, startswith, endswith, find, format.",
                    "join is the right way to combine many pieces: \",\".join(parts). Adding strings in a loop with + is slow because each + makes a new string.",
                    "f-strings are the modern way to format: f\"Hello {name}\". Clear and fast.",
                    "in checks substrings: \"py\" in \"python\" is True.",
                    "encode() turns str into bytes, decode() turns bytes into str - needed for files and networks.",
                ],
                "answer": "Strings are immutable Unicode sequences, so every change makes a new object. I format with f-strings, combine many parts with join instead of + in a loop, and use encode/decode when working with bytes.",
            },
            {
                "title": "2.6  List vs Tuple vs Set vs Dict",
                "what": "Choosing the right collection is about order, uniqueness, mutability and lookup speed.",
                "points": [
                    "List: ordered, mutable, allows duplicates, index access. Use for a changing sequence.",
                    "Tuple: ordered, immutable, allows duplicates, index access, hashable. Use for fixed records and dict keys.",
                    "Set: no order, mutable, unique items only, no index, O(1) membership. Use for uniqueness and fast \"in\" checks.",
                    "Dict: key to value mapping, keys unique, O(1) lookup by key, keeps insertion order. Use for lookups by name or id.",
                    "Speed of \"x in c\": list and tuple O(n); set and dict O(1) average.",
                    "Memory: tuple is the lightest; set and dict cost more because of the hash table.",
                ],
                "answer": "I pick by need: list for an ordered changing sequence, tuple for fixed data that may be a dict key, set for uniqueness and fast membership, dict for key-value lookup. Sets and dicts give O(1) search, lists and tuples give O(n).",
            },
            {
                "title": "2.7  Shallow Copy vs Deep Copy",
                "what": "A shallow copy copies only the outer object. A deep copy copies the outer object and everything inside it.",
                "points": [
                    "Plain assignment (b = a) copies nothing. Both names point to the same object.",
                    "Shallow copy: copy.copy(a), a.copy(), a[:] or list(a). It makes a new outer list, but the inner objects are still shared.",
                    "So after a shallow copy, changing an inner list in the copy also changes it in the original. This is a classic interview trap.",
                    "Deep copy: copy.deepcopy(a). It walks the whole structure and copies every level. Nothing is shared.",
                    "Deep copy is slower and uses more memory, so use it only when the data is nested and both sides must be fully independent.",
                    "For flat lists of numbers or strings, a shallow copy is enough, because those items are immutable anyway.",
                ],
                "answer": "Assignment shares the same object, shallow copy makes a new outer container but shares the inner objects, and deep copy copies every level so nothing is shared. For nested data that must be independent, I use copy.deepcopy().",
            },
        ],
    },
]
