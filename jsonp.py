# FIXME: POST, PUT, DELETE, HEAD, ... support
# FIXME: set response.set_header from r.headers
# FIXME: use requests.session
# FIXME: remote urls white list
# FIXME: catch requests exceptions

from bottle import get, abort, request, response
import requests

@get('/')
def jsonp():
    url = request.query.get('url') or abort()
    callback = request.query.get('callback') or abort()

    r = requests.get(url)
    response.status = r.status_code
    if r.ok:
        response.content_type = 'text/javascript'
        return "%s(%r);" % (callback, r.content)
    else:
        return r.content
