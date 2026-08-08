"""Content for SQL_Interview_Theory.docx.

Same rules as the Python notes: simple English, short sentences, theory that
can be memorised and spoken in an interview - PLUS a small example query per
topic (Sanket asked for examples on 09 Aug 2026).
Add one phase at a time, then run:  python build_docx.py sql
"""

DOC_TITLE = "SQL Interview Theory Notes"
DOC_SUBTITLE = "Simple English  |  Theory + small examples  |  Sanket Kolhe"

CONTENT = [
    {
        "phase": "SQL Phase 1 - Basics",
        "topics": [
            {
                "title": "S1.1  What is SQL, Database, DBMS vs RDBMS",
                "what": "SQL (Structured Query Language) is the standard language to store, read and manage data kept in a relational database.",
                "points": [
                    "Database: an organized collection of data. DBMS: the software that manages it (create, read, update, delete, security).",
                    "RDBMS: a DBMS that keeps data in tables (rows and columns) with relationships between tables. Examples: MySQL, PostgreSQL, SQL Server, Oracle.",
                    "Non-relational (NoSQL) systems like MongoDB or Redis store documents or key-value pairs instead of tables.",
                    "In an RDBMS, every table has columns (fields with a type) and rows (records). Tables link to each other using keys.",
                    "SQL is declarative: we say WHAT data we want, and the database engine decides HOW to fetch it.",
                    "SQL is mostly the same everywhere, with small dialect differences (LIMIT vs TOP, AUTO_INCREMENT vs SERIAL).",
                ],
                "example": "SELECT name, city FROM customers WHERE city = 'Surat';",
                "answer": "SQL is the standard declarative language for relational databases. A DBMS manages data; an RDBMS like MySQL or PostgreSQL stores it in related tables of rows and columns, linked by keys. We describe what we want, and the engine plans how to get it.",
            },
            {
                "title": "S1.2  SQL Command Types - DDL, DML, DQL, DCL, TCL",
                "what": "SQL commands are grouped by what they touch: structure, data, permissions, or transactions.",
                "points": [
                    "DDL (Data Definition Language) - changes structure: CREATE, ALTER, DROP, TRUNCATE. Usually auto-committed.",
                    "DML (Data Manipulation Language) - changes data: INSERT, UPDATE, DELETE. Can be rolled back inside a transaction.",
                    "DQL (Data Query Language) - reads data: SELECT.",
                    "DCL (Data Control Language) - permissions: GRANT, REVOKE.",
                    "TCL (Transaction Control Language) - transactions: COMMIT, ROLLBACK, SAVEPOINT.",
                    "Interview line: \"TRUNCATE is DDL, DELETE is DML\" - that is why TRUNCATE is faster and usually cannot be rolled back.",
                ],
                "example": "CREATE TABLE orders (id INT);   -- DDL\nINSERT INTO orders VALUES (1); -- DML\nSELECT * FROM orders;          -- DQL\nGRANT SELECT ON orders TO ravi;-- DCL\nCOMMIT;                        -- TCL",
                "answer": "DDL defines structure (CREATE, ALTER, DROP, TRUNCATE), DML changes data (INSERT, UPDATE, DELETE), DQL is SELECT, DCL handles permissions (GRANT, REVOKE), and TCL manages transactions (COMMIT, ROLLBACK). DELETE is DML and can roll back; TRUNCATE is DDL.",
            },
            {
                "title": "S1.3  Common Data Types",
                "what": "Every column has a data type that decides what values it can hold and how much space it takes.",
                "points": [
                    "Whole numbers: INT / BIGINT (bigger range). SMALLINT / TINYINT for small ranges.",
                    "Exact decimals: DECIMAL(10,2) - use for money, never FLOAT, because FLOAT rounds.",
                    "Approximate: FLOAT / DOUBLE - for scientific values where tiny rounding is fine.",
                    "Text: CHAR(n) fixed length, VARCHAR(n) variable up to n, TEXT for long free text.",
                    "Date and time: DATE, TIME, DATETIME / TIMESTAMP (timestamp often auto-updates and is timezone-aware in Postgres).",
                    "BOOLEAN (true/false; MySQL stores it as TINYINT(1)).",
                    "Others: JSON for flexible data, BLOB for binary files, UUID for unique ids.",
                    "Right type = less space, faster index, and built-in validation.",
                ],
                "example": "CREATE TABLE products (\n  id INT PRIMARY KEY,\n  name VARCHAR(100),\n  price DECIMAL(10,2),\n  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);",
                "answer": "Main families are integers (INT, BIGINT), exact decimals (DECIMAL - always for money), floats, text (CHAR, VARCHAR, TEXT), date/time (DATE, DATETIME, TIMESTAMP), boolean, and JSON/BLOB. Choosing the smallest correct type saves space and speeds up indexes.",
            },
            {
                "title": "S1.4  Constraints - NOT NULL, UNIQUE, CHECK, DEFAULT",
                "what": "A constraint is a rule on a column that the database itself enforces, so bad data can never enter.",
                "points": [
                    "NOT NULL: the column must always have a value.",
                    "UNIQUE: no two rows can have the same value in this column (NULLs are usually allowed and repeatable).",
                    "CHECK: a custom condition, like price >= 0 or status IN ('new','paid').",
                    "DEFAULT: the value used when the INSERT does not give one.",
                    "PRIMARY KEY and FOREIGN KEY are also constraints (next topic).",
                    "Why in the DB and not only in app code: many apps and scripts touch the same tables - the database is the last line of defense.",
                    "Constraints can be added later with ALTER TABLE, but existing bad data must be fixed first.",
                ],
                "example": "CREATE TABLE users (\n  email VARCHAR(255) NOT NULL UNIQUE,\n  age INT CHECK (age >= 18),\n  status VARCHAR(10) DEFAULT 'active'\n);",
                "answer": "Constraints are database-enforced rules: NOT NULL requires a value, UNIQUE forbids duplicates, CHECK applies a custom condition, DEFAULT fills missing values. They protect data quality even when many different apps write to the table.",
            },
            {
                "title": "S1.5  Primary Key vs Foreign Key",
                "what": "A primary key uniquely identifies each row in its own table; a foreign key points to a primary key in another table to connect them.",
                "points": [
                    "Primary key: unique + NOT NULL, one per table (can be one column or a composite of several). Usually an auto-increment id.",
                    "Foreign key: a column whose values must exist in the referenced table's key - this is referential integrity.",
                    "Example: orders.customer_id references customers.id - an order cannot belong to a customer that does not exist.",
                    "The DB blocks deleting a parent row that children still point to, unless we choose: ON DELETE CASCADE (delete children too), SET NULL, or RESTRICT (default block).",
                    "Foreign keys are how one-to-many and many-to-many (via a junction table) relationships are built.",
                    "Auto-increment ids: AUTO_INCREMENT (MySQL), SERIAL / IDENTITY (Postgres).",
                ],
                "example": "CREATE TABLE orders (\n  id INT PRIMARY KEY AUTO_INCREMENT,\n  customer_id INT,\n  FOREIGN KEY (customer_id) REFERENCES customers(id)\n    ON DELETE CASCADE\n);",
                "answer": "A primary key is the unique, non-null identifier of a row; a foreign key stores another table's primary key to link rows and enforce referential integrity - the DB rejects orphan records, and ON DELETE CASCADE/SET NULL/RESTRICT controls what happens when the parent goes.",
            },
            {
                "title": "S1.6  NULL - Behavior, IS NULL, COALESCE",
                "what": "NULL means \"value unknown or missing\". It is not zero, not an empty string, and it behaves specially in every comparison.",
                "points": [
                    "Any comparison with NULL gives NULL (unknown), not true or false: salary = NULL never matches.",
                    "Correct check: IS NULL / IS NOT NULL.",
                    "NULL = NULL is also unknown - two unknowns are not \"equal\".",
                    "Aggregates skip NULLs: COUNT(col) ignores them, but COUNT(*) counts every row. AVG divides only by non-null count.",
                    "NOT IN with a NULL inside the list matches nothing - a classic silent bug.",
                    "COALESCE(a, b, c) returns the first non-null value - the standard way to give defaults in queries.",
                    "In WHERE, rows with NULL in the condition simply drop out - they are neither true nor false.",
                ],
                "example": "SELECT name, COALESCE(phone, 'no phone') AS phone\nFROM customers\nWHERE deleted_at IS NULL;",
                "answer": "NULL means unknown, so any comparison with it returns unknown - we must use IS NULL, not = NULL. Aggregates like COUNT(col) and AVG skip NULLs, NOT IN breaks silently if the list contains a NULL, and COALESCE gives the first non-null value as a default.",
            },
        ],
    },
    {
        "phase": "SQL Phase 2 - Core Queries",
        "topics": [
            {
                "title": "S2.1  SELECT, WHERE and Operators (IN, BETWEEN, LIKE)",
                "what": "SELECT chooses columns, FROM names the table, and WHERE filters rows with conditions.",
                "points": [
                    "SELECT * takes all columns - fine for exploring, avoided in production code (wastes I/O, breaks when columns change).",
                    "Comparison operators: =, <> (not equal), >, <, >=, <=. Combine with AND, OR, NOT - use brackets to keep OR logic clear.",
                    "IN: value matches any item in a list - cleaner than many ORs.",
                    "BETWEEN a AND b: inclusive range, works for numbers and dates.",
                    "LIKE with wildcards: % = any characters, _ = exactly one. 'Sa%' starts with Sa. ILIKE in Postgres ignores case.",
                    "Logical order of a query: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT. (That is why WHERE cannot see SELECT aliases.)",
                ],
                "example": "SELECT name, price FROM products\nWHERE category IN ('shirt','kurti')\n  AND price BETWEEN 500 AND 2000\n  AND name LIKE 'Cotton%';",
                "answer": "SELECT picks columns and WHERE filters rows using =, <>, IN for lists, BETWEEN for inclusive ranges, and LIKE with % and _ wildcards for patterns. Logically the engine runs FROM, WHERE, GROUP BY, HAVING, SELECT, then ORDER BY - which explains why WHERE cannot use SELECT aliases.",
            },
            {
                "title": "S2.2  DISTINCT, ORDER BY, LIMIT / OFFSET",
                "what": "DISTINCT removes duplicate rows, ORDER BY sorts the result, and LIMIT/OFFSET take just a slice of it.",
                "points": [
                    "SELECT DISTINCT city FROM customers - each city once. It applies to the whole selected row, not one column alone.",
                    "COUNT(DISTINCT city) counts unique values.",
                    "ORDER BY col ASC|DESC; multiple keys allowed: ORDER BY city, price DESC. Without ORDER BY, row order is never guaranteed.",
                    "Sorting can also use expressions or aliases: ORDER BY total DESC.",
                    "LIMIT n returns the first n rows; OFFSET m skips m first - together they give pagination (page 3 of size 20: LIMIT 20 OFFSET 40).",
                    "Dialects: MySQL/Postgres use LIMIT; SQL Server uses TOP n or OFFSET ... FETCH.",
                    "Big OFFSETs get slow (engine still walks the skipped rows) - keyset pagination (WHERE id > last_seen) scales better.",
                ],
                "example": "SELECT DISTINCT city FROM customers;\n\nSELECT name, price FROM products\nORDER BY price DESC\nLIMIT 10 OFFSET 20;   -- page 3, 10 per page",
                "answer": "DISTINCT de-duplicates the selected rows, ORDER BY sorts (multiple keys, ASC/DESC), and LIMIT with OFFSET slices for pagination. Row order is undefined without ORDER BY, and for deep pages keyset pagination beats large OFFSETs.",
            },
            {
                "title": "S2.3  Aggregate Functions - COUNT, SUM, AVG, MIN, MAX",
                "what": "Aggregate functions squeeze many rows into one summary value.",
                "points": [
                    "COUNT(*) counts rows; COUNT(col) counts non-null values in that column; COUNT(DISTINCT col) counts unique values.",
                    "SUM adds, AVG averages, MIN/MAX give extremes (also work on text and dates).",
                    "All except COUNT(*) ignore NULLs - AVG divides by the non-null count only.",
                    "Without GROUP BY, the whole result is one row.",
                    "An aggregate cannot go in WHERE (WHERE runs before grouping) - filtering on aggregates belongs in HAVING.",
                    "Mixing aggregated and normal columns needs GROUP BY on the normal ones.",
                ],
                "example": "SELECT COUNT(*) AS orders_count,\n       SUM(amount) AS revenue,\n       AVG(amount) AS avg_order,\n       MAX(amount) AS biggest\nFROM orders\nWHERE status = 'paid';",
                "answer": "COUNT, SUM, AVG, MIN and MAX collapse many rows into one summary. COUNT(*) counts rows while COUNT(col) skips NULLs, all aggregates ignore NULLs otherwise, and conditions on aggregates go in HAVING because WHERE runs before aggregation.",
            },
            {
                "title": "S2.4  GROUP BY and HAVING",
                "what": "GROUP BY makes one summary row per group, and HAVING filters those groups after aggregation.",
                "points": [
                    "GROUP BY city gives one row per city; aggregates then work inside each group.",
                    "Rule: every column in SELECT must be either aggregated or listed in GROUP BY.",
                    "WHERE filters rows BEFORE grouping; HAVING filters groups AFTER - both can appear in one query.",
                    "HAVING can use aggregates: HAVING COUNT(*) > 5. WHERE cannot.",
                    "Grouping by several columns makes one row per combination: GROUP BY city, category.",
                    "Order of writing: FROM, WHERE, GROUP BY, HAVING, ORDER BY.",
                    "Put as much filtering as possible into WHERE - fewer rows to group means a faster query.",
                ],
                "example": "SELECT city, COUNT(*) AS customers\nFROM customers\nWHERE status = 'active'\nGROUP BY city\nHAVING COUNT(*) >= 10\nORDER BY customers DESC;",
                "answer": "GROUP BY collapses rows into one row per group so aggregates work per group, and HAVING filters those groups on aggregate conditions. WHERE filters rows before grouping, HAVING after - and pushing filters into WHERE keeps queries fast.",
            },
            {
                "title": "S2.5  Common String and Date Functions",
                "what": "Built-in functions transform text and dates right inside the query.",
                "points": [
                    "Text: CONCAT joins, UPPER/LOWER change case, TRIM cuts spaces, LENGTH counts, SUBSTRING cuts a part, REPLACE swaps text.",
                    "Search inside text: LOCATE/POSITION or LIKE.",
                    "Dates: NOW()/CURRENT_TIMESTAMP for current moment, CURRENT_DATE for today.",
                    "Parts of a date: EXTRACT(YEAR FROM col) or YEAR(col)/MONTH(col) in MySQL.",
                    "Date maths: DATE_ADD/DATE_SUB (MySQL), col + INTERVAL '7 days' (Postgres), DATEDIFF for gaps.",
                    "Formatting: DATE_FORMAT (MySQL) / TO_CHAR (Postgres) turn dates into display text.",
                    "Careful: wrapping an indexed column in a function (WHERE YEAR(created_at) = 2026) blocks the index - better use a range: created_at >= '2026-01-01' AND < '2027-01-01'.",
                ],
                "example": "SELECT CONCAT(first_name, ' ', last_name) AS full_name,\n       UPPER(city) AS city,\n       EXTRACT(YEAR FROM created_at) AS joined_year\nFROM customers\nWHERE created_at >= NOW() - INTERVAL '30 days';",
                "answer": "Everyday functions: CONCAT, UPPER/LOWER, TRIM, SUBSTRING, REPLACE for text; NOW, EXTRACT, DATE_ADD/INTERVAL, DATEDIFF for dates. One performance rule: never wrap an indexed column in a function inside WHERE - rewrite it as a range so the index still works.",
            },
            {
                "title": "S2.6  CASE Expression",
                "what": "CASE is SQL's if/else - it returns different values based on conditions, inside any query.",
                "points": [
                    "Searched form: CASE WHEN cond1 THEN x WHEN cond2 THEN y ELSE z END. Conditions are checked top to bottom, first match wins.",
                    "Simple form: CASE status WHEN 'P' THEN 'Paid' WHEN 'N' THEN 'New' END - compares one column to values.",
                    "Without ELSE, non-matching rows get NULL.",
                    "Works in SELECT (labels/buckets), ORDER BY (custom sort order), and inside aggregates.",
                    "Conditional counting trick: SUM(CASE WHEN status='paid' THEN 1 ELSE 0 END) - counts per condition in one pass; FILTER (Postgres) does the same.",
                    "This pivot-style trick turns row values into columns - a very common interview ask.",
                ],
                "example": "SELECT name,\n  CASE\n    WHEN price < 500 THEN 'budget'\n    WHEN price < 2000 THEN 'regular'\n    ELSE 'premium'\n  END AS price_band\nFROM products;",
                "answer": "CASE is an inline if/else: WHEN conditions are checked in order and the first match returns its value, ELSE catches the rest. I use it for bucketing values, custom sort orders, and the SUM(CASE WHEN...) trick to count several conditions in a single scan.",
            },
        ],
    },
]
