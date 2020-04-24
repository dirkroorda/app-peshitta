from os.path import dirname, abspath

API_VERSION = 1

PROVENANCE_SPEC = dict(
    org="etcbc",
    repo="peshitta",
    version="0.1",
    doi="10.5281/zenodo.1463675",
    corpus="Peshitta (Old Testament)",
    webBase="{urlGh}/{org}/{repo}/blob/master/source",
    webUrl="/{version}/<1>",
    webHint="Show this document in the Peshitta repository",
)

DOCS = dict(
    docPage="transcription",
    featureBase="{docBase}/transcription-{version}{docExt}#{feature}",
    featurePage="",
)

DATA_DISPLAY = dict(noneValues={None, "NA", "none", "unknown"}, writing="syc")

TYPE_DISPLAY = dict()

INTERFACE_DEFAULTS = dict()


def deliver():
    return (globals(), dirname(abspath(__file__)))
