from tf.applib.helpers import dh
from tf.applib.api import setupApi
from tf.applib.links import outLink

PLAIN_LINK = "https://github.com/{org}/{repo}/blob/master/source/{version}/{book}"


def notice(app):
    if int(app.api.TF.version.split(".")[0]) <= 7:
        print(
            f"""
Your Text-Fabric is outdated.
It cannot load this version of the TF app `{app.appName}`.
Recommendation: upgrade Text-Fabric to version 8.
Hint:

    pip3 install --upgrade text-fabric

"""
        )


class TfApp(object):
    def __init__(app, *args, **kwargs):
        setupApi(app, *args, **kwargs)
        notice(app)

    def webLink(app, n, text=None, clsName=None, _asString=False, _noUrl=False):
        api = app.api
        T = api.T
        version = app.version

        (book, chapter, verse) = T.sectionFromNode(n, fillup=True)
        passageText = app.sectionStrFromNode(n)
        href = (
            "#"
            if _noUrl
            else PLAIN_LINK.format(
                org=app.org, repo=app.repo, version=version, book=book,
            )
        )
        if text is None:
            text = passageText
            title = "show this passage in the Peshitta source"
        else:
            title = passageText
        if _noUrl:
            title = None
        target = "" if _noUrl else None
        result = outLink(
            text,
            href,
            title=title,
            clsName=clsName,
            target=target,
            passage=passageText,
        )
        if _asString:
            return result
        dh(result)
