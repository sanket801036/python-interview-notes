"""Content for React_Interview_Theory.docx.

3-YOE depth, simple English, small JSX example per topic. Function components
and hooks only (class components mentioned where interviewers still ask).
Run:  python build_docx.py react
"""

DOC_TITLE = "React Interview Theory Notes"
DOC_SUBTITLE = "3-YOE depth  |  Hooks-first + examples  |  Sanket Kolhe"

CONTENT = [
    {
        "phase": "React Phase 1 - Fundamentals",
        "topics": [
            {
                "title": "R1.1  What is React - Virtual DOM and JSX",
                "what": "React is a JavaScript library for building UIs from components; it re-renders efficiently by diffing a virtual DOM instead of touching the real DOM directly.",
                "points": [
                    "Library, not a full framework: React handles the view; routing, data fetching etc. come from the ecosystem (Router, React Query...).",
                    "Declarative model: UI = f(state). We describe what the UI looks like for a state; React updates the DOM when state changes - no manual DOM manipulation.",
                    "Virtual DOM: a lightweight JS copy of the UI tree. On state change React builds the new tree, diffs it with the old one (reconciliation), and applies only the minimal real-DOM changes - because real DOM operations are the slow part.",
                    "JSX: HTML-like syntax inside JS that compiles to function calls (React.createElement / the JSX runtime). It is just JavaScript - hence className, camelCase props and {expressions}.",
                    "Components are plain functions returning JSX; data flows one way, parent to child - predictable and debuggable.",
                    "React alone renders in the browser; Next.js adds server-side rendering; React Native maps the same model to native mobile views.",
                ],
                "example": "function App() {\n  const [count, setCount] = useState(0);\n  return (\n    <button onClick={() => setCount(count + 1)}>\n      Clicked {count} times\n    </button>\n  );\n}",
                "answer": "React is a component-based UI library with a declarative model - UI is a function of state. On updates it diffs a virtual DOM and patches only what changed, since real DOM writes are expensive. JSX is syntax sugar over function calls, data flows one way, and the same model powers React Native on mobile.",
            },
            {
                "title": "R1.2  Components and Props",
                "what": "A component is a reusable function returning JSX; props are the read-only inputs a parent passes down.",
                "points": [
                    "function OrderCard({ order, onCancel }) - destructured props: data plus callback functions.",
                    "Props are immutable inside the child - changing data means the PARENT changes its state and passes new props. One-way data flow.",
                    "Child talks to parent via callback props (onCancel) - the child calls it, the parent owns the logic. This pair of ideas answers most 'component communication' questions.",
                    "props.children renders whatever the parent nests inside - the composition primitive for wrappers, layouts, modals.",
                    "Component names must be Capitalized - lowercase means an HTML tag to JSX.",
                    "Default values via destructuring defaults ({ limit = 10 }); TypeScript interfaces (or PropTypes) document the contract.",
                    "Keep components small and single-purpose; extract when JSX or logic grows - reuse and testing both improve.",
                ],
                "example": "function OrderCard({ order, onCancel }) {\n  return (\n    <div className=\"card\">\n      <b>{order.id}</b> - {order.amount}\n      <button onClick={() => onCancel(order.id)}>\n        Cancel\n      </button>\n    </div>\n  );\n}",
                "answer": "Components are functions returning JSX; props are their read-only inputs flowing parent to child. Children never mutate props - they signal the parent through callback props, and the parent updates state. children enables composition, and small single-purpose components keep the tree testable.",
            },
            {
                "title": "R1.3  State - useState and Immutability",
                "what": "State is a component's own changing data; setState triggers a re-render, and updates must be immutable.",
                "points": [
                    "const [items, setItems] = useState([]) - state survives re-renders; a plain variable resets every render.",
                    "Calling the setter re-renders the component and its children with the new value.",
                    "Never mutate: items.push(x) changes the same array - React compares by reference (Object.is), sees the same reference, and may skip the re-render. Always create new: setItems([...items, x]).",
                    "Objects: setUser({ ...user, name: \"New\" }) - spread and override.",
                    "Updates are batched and asynchronous - reading state right after setting it gives the old value.",
                    "Consecutive updates need the functional form: setCount(c => c + 1) twice really adds 2; setCount(count + 1) twice adds 1 (stale value).",
                    "Lazy initialization: useState(() => expensive()) runs the initializer once, not every render.",
                ],
                "example": "const [items, setItems] = useState([]);\n// wrong: items.push(x); setItems(items)\nsetItems(prev => [...prev, x]);   // right\nsetUser(prev => ({ ...prev,\n                   name: \"Sanket\" }));",
                "answer": "useState keeps data across renders and its setter schedules a re-render. Updates must be immutable - spread into new arrays/objects - because React detects change by reference. Setters are batched, so consecutive updates use the functional form setX(prev => ...), and expensive initial values go in a lazy initializer.",
            },
            {
                "title": "R1.4  Rendering, Reconciliation and Keys",
                "what": "On state change React re-runs the component, diffs the new element tree against the old, and patches the DOM - keys tell the diff which list items are which.",
                "points": [
                    "Re-render = re-running the function to get new JSX; it does NOT mean DOM rebuild - the diff decides actual DOM work.",
                    "A parent re-render re-renders children by default (unless memoized) - worth saying, it surprises people.",
                    "Reconciliation heuristics: same element type -> update in place; different type -> unmount and rebuild the subtree.",
                    "Lists need stable keys: key lets React match old and new items, preserving state and DOM per item.",
                    "Index as key breaks on insert/remove/reorder: items shift indexes, React matches the wrong pairs - input text and animations jump to wrong rows. Use a stable id.",
                    "Key changes force remount - sometimes used deliberately (key={userId} to reset a form).",
                    "React 18 batches multiple setStates (even in promises/timeouts) into one render pass.",
                ],
                "example": "{orders.map(o => (\n  <OrderCard key={o.id} order={o} />\n))}\n// key={index} bugs: reorder/delete\n// pairs state with the wrong row",
                "answer": "State changes re-run the component and React diffs the element trees, patching only real changes - same type updates in place, different type remounts. Keys give list items identity across renders; index keys corrupt item state on reorder or delete, so I use stable ids, and a deliberate key change is a clean way to reset a subtree.",
            },
            {
                "title": "R1.5  Conditional Rendering and Lists",
                "what": "JSX composes UI with plain JS expressions - ternaries and && for conditions, map for lists.",
                "points": [
                    "Ternary for either/or: {loading ? <Spinner /> : <List items={items} />}.",
                    "&& for show/hide: {error && <Alert msg={error} />} - renders nothing when falsy.",
                    "The 0 gotcha: {items.length && <List/>} renders a literal 0 when empty - use items.length > 0 or a ternary.",
                    "Returning null renders nothing - a valid way for a component to hide itself.",
                    "Lists are map() with keys; filter().map() chains for filtered views.",
                    "Standard page pattern: three branches - loading, error, data (with an empty-state for zero items).",
                    "Heavy nesting of ternaries is a smell - extract small components or early-return variants.",
                ],
                "example": "if (loading) return <Spinner />;\nif (error) return <Alert msg={error} />;\nreturn items.length > 0 ? (\n  <ul>{items.map(i =>\n    <li key={i.id}>{i.name}</li>)}</ul>\n) : (\n  <p>No items yet</p>\n);",
                "answer": "Conditions are plain JS in JSX - ternaries for either/or, && for optional blocks (guarding the classic 0-renders bug with an explicit comparison), null to render nothing. Lists are map with stable keys, and every data view gets the loading / error / empty / data branches.",
            },
            {
                "title": "R1.6  Forms - Controlled vs Uncontrolled",
                "what": "A controlled input's value lives in React state and updates via onChange; an uncontrolled input keeps its own DOM state, read via a ref.",
                "points": [
                    "Controlled: value={name} onChange={e => setName(e.target.value)} - state is the single source of truth.",
                    "Controlled benefits: instant validation, disabling submit, formatting as-you-type, conditional fields - full control per keystroke.",
                    "Uncontrolled: defaultValue + ref, read at submit - less code, fewer re-renders, fine for simple forms; also file inputs are inherently uncontrolled.",
                    "One object state for multi-field forms: setForm({ ...form, [e.target.name]: e.target.value }).",
                    "onSubmit handler with e.preventDefault() - stop the browser page reload.",
                    "Real projects reach for react-hook-form (uncontrolled + refs = performant) with schema validation (zod/yup) - worth naming.",
                    "Every-keystroke re-renders on huge forms are the controlled approach's cost - that is exactly what react-hook-form avoids.",
                ],
                "example": "const [form, setForm] = useState({ email: \"\" });\nconst change = e => setForm({ ...form,\n  [e.target.name]: e.target.value });\n\n<form onSubmit={e => { e.preventDefault();\n                       submit(form); }}>\n  <input name=\"email\" value={form.email}\n         onChange={change} />\n</form>",
                "answer": "Controlled inputs bind value to state with onChange - the React-idiomatic way, enabling live validation and dynamic form logic at the cost of re-rendering per keystroke. Uncontrolled inputs stay in the DOM and are read via refs - simpler and faster for big or basic forms, which is why react-hook-form builds on them with schema validation on top.",
            },
            {
                "title": "R1.7  useEffect as the Lifecycle",
                "what": "useEffect runs side effects after render - with the dependency array replacing mount/update/unmount lifecycle thinking.",
                "points": [
                    "Effects are for touching the outside world: fetching, subscriptions, timers, document title - never for computing render data.",
                    "useEffect(fn, []) - after first render only (the componentDidMount analog).",
                    "useEffect(fn, [id]) - after renders where id changed.",
                    "No array - after every render (rarely wanted).",
                    "The return function is cleanup: runs before the next effect execution and at unmount - clearing timers, aborting fetches, unsubscribing.",
                    "Class mapping (asked in interviews): componentDidMount/DidUpdate/WillUnmount all collapse into effect + deps + cleanup.",
                    "StrictMode in dev mounts-unmounts-mounts once to expose missing cleanup - effects must be written idempotent.",
                    "Better mental model: 'synchronize this component with an external system whenever these values change', not 'lifecycle hooks'.",
                ],
                "example": "useEffect(() => {\n  const t = setInterval(tick, 1000);\n  return () => clearInterval(t); // cleanup\n}, []);   // mount + unmount only",
                "answer": "useEffect runs after render for outside-world work - fetching, timers, subscriptions - controlled by its dependency array: [] once, [x] when x changes. The returned cleanup runs before re-execution and at unmount, replacing all three class lifecycle methods. The real model is synchronization with external systems, and StrictMode's double-mount catches missing cleanup.",
            },
        ],
    },
]
