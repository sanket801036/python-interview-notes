"""Build interview-notes .docx files from content modules.

Writes the OOXML by hand (zipfile + stdlib) so no external library is needed.
Layout is tuned for printing: 9 pt body text, narrow margins, tight spacing.
Topics may carry an optional "example" field, rendered as a monospace code box.

Run:  python build_docx.py            (builds every doc listed in DOCS)
      python build_docx.py sql       (builds only that one)
"""

import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).parent

# key -> (content module name, output file name)
DOCS = {
    "python": ("notes_content", "Python_Interview_Theory.docx"),
    "sql": ("sql_content", "SQL_Interview_Theory.docx"),
    "django": ("django_content", "Django_Interview_Theory.docx"),
    "fastapi": ("fastapi_content", "FastAPI_Interview_Theory.docx"),
}

# sizes are in half-points (18 = 9 pt); spacing and indents are in twips (1/20 pt)
BODY_SZ = 18
CODE_SZ = 17
H1_SZ = 26
H2_SZ = 21
TITLE_SZ = 36
LABEL_COLOR = "1F4E79"
ANSWER_COLOR = "2E5E1F"
CODE_COLOR = "3B3B3B"

NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"')


def run(text, *, bold=False, italic=False, size=BODY_SZ, color=None, mono=False):
    props = ""
    if mono:
        props += '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas" w:cs="Consolas"/>'
    if bold:
        props += "<w:b/>"
    if italic:
        props += "<w:i/>"
    if color:
        props += f'<w:color w:val="{color}"/>'
    props += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    return (
        f"<w:r><w:rPr>{props}</w:rPr>"
        f'<w:t xml:space="preserve">{escape(text)}</w:t></w:r>'
    )


def para(runs, *, before=0, after=40, indent=0, hanging=0, border=False,
         align=None, shade=None):
    pr = "<w:pPr>"
    if align:
        pr += f'<w:jc w:val="{align}"/>'
    if indent or hanging:
        pr += f'<w:ind w:left="{indent}" w:hanging="{hanging}"/>'
    pr += f'<w:spacing w:before="{before}" w:after="{after}" w:line="230" w:lineRule="auto"/>'
    if border:
        pr += ('<w:pBdr><w:left w:val="single" w:sz="12" w:space="4" '
               f'w:color="{ANSWER_COLOR}"/></w:pBdr>')
    if shade:
        pr += f'<w:shd w:val="clear" w:color="auto" w:fill="{shade}"/>'
    pr += "</w:pPr>"
    return f"<w:p>{pr}{''.join(runs)}</w:p>"


def build_body(content, title, subtitle) -> str:
    parts = [
        para([run(title, bold=True, size=TITLE_SZ, color=LABEL_COLOR)],
             after=20, align="center"),
        para([run(subtitle, italic=True, size=BODY_SZ)],
             after=160, align="center"),
    ]

    for phase in content:
        parts.append(
            para([run(phase["phase"], bold=True, size=H1_SZ, color=LABEL_COLOR)],
                 before=200, after=60)
        )
        for topic in phase["topics"]:
            parts.append(
                para([run(topic["title"], bold=True, size=H2_SZ)],
                     before=140, after=40)
            )
            parts.append(
                para([run("What it is:  ", bold=True), run(topic["what"])],
                     after=40)
            )
            for point in topic["points"]:
                parts.append(
                    para([run("•   "), run(point)],
                         indent=260, hanging=200, after=25)
                )
            example_lines = topic.get("example", "").splitlines()
            for i, line in enumerate(example_lines):
                runs = []
                if i == 0:
                    runs.append(run("Example:  ", bold=True, size=CODE_SZ))
                runs.append(run(line, mono=True, size=CODE_SZ, color=CODE_COLOR))
                parts.append(
                    para(runs, indent=260, after=15, shade="F2F2F2")
                )
            parts.append(
                para([run("Interview answer:  ", bold=True, color=ANSWER_COLOR),
                      run(topic["answer"], italic=True)],
                     before=50, after=110, indent=120, border=True)
            )

    parts.append(
        '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>'
        '<w:pgMar w:top="620" w:right="620" w:bottom="620" w:left="620" '
        'w:header="0" w:footer="0" w:gutter="0"/></w:sectPr>'
    )
    return "".join(parts)


DOCUMENT = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    f"<w:document {NS}><w:body>{{body}}</w:body></w:document>"
)

STYLES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    f"<w:styles {NS}><w:docDefaults><w:rPrDefault><w:rPr>"
    '<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>'
    f'<w:sz w:val="{BODY_SZ}"/><w:szCs w:val="{BODY_SZ}"/>'
    "</w:rPr></w:rPrDefault><w:pPrDefault><w:pPr>"
    '<w:spacing w:after="40" w:line="230" w:lineRule="auto"/>'
    "</w:pPr></w:pPrDefault></w:docDefaults>"
    '<w:style w:type="paragraph" w:default="1" w:styleId="Normal">'
    '<w:name w:val="Normal"/></w:style></w:styles>'
)

CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>'
    "</Types>"
)

RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
    "</Relationships>"
)

DOC_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>'
    "</Relationships>"
)


def build_one(key):
    module_name, out_name = DOCS[key]
    try:
        module = __import__(module_name)
    except ImportError:
        print(f"skip {key}: {module_name}.py not found")
        return

    out = HERE / out_name
    body = build_body(module.CONTENT, module.DOC_TITLE, module.DOC_SUBTITLE)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/document.xml", DOCUMENT.format(body=body))

    topics = sum(len(p["topics"]) for p in module.CONTENT)
    print(f"Wrote {out.name}  ({len(module.CONTENT)} phase(s), {topics} topic(s))")


if __name__ == "__main__":
    keys = sys.argv[1:] or list(DOCS)
    for key in keys:
        build_one(key)
