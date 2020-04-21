from os.path import dirname, abspath

API_VERSION = 1

PROTOCOL = "http://"
HOST = "localhost"
PORT = dict(kernel=18982, web=8102)

ORG = "etcbc"
REPO = "peshitta"
CORPUS = "Peshitta (Old Testament)"
VERSION = "0.1"
RELATIVE = "tf"

DOI_TEXT = "10.5281/zenodo.1463675"
DOI_URL = "https://doi.org/10.5281/zenodo.1463675"

DOC_URL = f"https://github.com/{ORG}/{REPO}/blob/master/docs"
DOC_INTRO = "transcription.md"
CHAR_URL = "{tfDoc}/Writing/Syriac"
CHAR_TEXT = ("Syriac characters and transcriptions",)

FEATURE_URL = f"{DOC_URL}/transcription-{{version}}.md#{{feature}}"

MODULE_SPECS = ()

ZIP = [REPO]

BASE_TYPE = "word"
CONDENSE_TYPE = "verse"

NONE_VALUES = {None, "NA", "none", "unknown"}

STANDARD_FEATURES = """
    word word_etcbc
    trailer trailer_etcbc
    book book@en
    chapter verse
""".strip().split()

EXCLUDED_FEATURES = set()

NO_DESCEND_TYPES = {"lex"}

EXAMPLE_SECTION = (
    f"<code>Genesis 1:1</code> (use"
    f' <a href="https://github.com/{ORG}/{REPO}'
    f'/blob/master/tf/{VERSION}/book%40en.tf" target="_blank">'
    f"English book names</a>)"
)
EXAMPLE_SECTION_TEXT = "Genesis 1:1"

SECTION_SEP1 = " "
SECTION_SEP2 = ":"

WRITING = "syc"
WRITING_DIR = "rtl"

FONT_NAME = "Estrangelo Edessa"
FONT = "SyrCOMEdessa.otf"
FONTW = "SyrCOMEdessa.woff"

TEXT_FORMATS = {}

BROWSE_NAV_LEVEL = 2
BROWSE_CONTENT_PRETTY = False

VERSE_TYPES = None

LEX = None

TRANSFORM = None

CHILD_TYPE = dict(book="chapter", chapter="verse", verse="word")

SUPER_TYPE = None

TYPE_DISPLAY = dict(
    book=dict(
        template="{book}",
        bareFeatures="",
        features="",
        level=3, flow="col", wrap=False, stretch=False,
    ),
    chapter=dict(
        template="{chapter}",
        bareFeatures="",
        features="",
        level=3, flow="col", wrap=False, strectch=False,
    ),
    verse=dict(
        template="{verse}",
        bareFeatures="",
        features="",
        level=2, flow="row", wrap=True, strectch=True,
    ),
    word=dict(
        template=True,
        bareFeatures="",
        features="",
        level=0, flow="col", wrap=False, strectch=False,
    ),
)

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
