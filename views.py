from config import ENCODING, TEMPLATES


def get_content(view, templates=TEMPLATES):
    with open(templates[view], 'rb') as content:
        return content.read()


def index(view, environ, templates=TEMPLATES):
    content = get_content(view, templates)
    return content


def login(view, environ, templates=TEMPLATES):
    return get_content(view, templates)


def private(view, environ, templates=TEMPLATES):
    if environ.get('HTTP_AUTHORIZATION'):
        return get_content(view,templates)
    else:
        return b'Access denied.'