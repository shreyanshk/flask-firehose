def test_push_doc0a(tapp):
    resp = tapp.get('/doc1a')
    assert resp.headers['Link'] == '</static/css/main.css>; as=style; rel=preload, '


def test_push_doc1b(tapp):
    resp = tapp.get('/doc1b')
    assert resp.headers['Link'] == ('</static/js/vendor/modernizr-3.5.0.min.js>; rel=preload, '
                                    '</static/css/main.css>; as=style; rel=preload, ')


def test_push_doc2(tapp):
    resp = tapp.get('/doc2')
    assert resp.headers['Link'] == '</static/js/vendor/modernizr-3.5.0.min.js>; rel=preload, '


# tests to make sure subsequent requests do not push again
def test_push_doc1a_s(tapp):
    resp = tapp.get('/doc1a')
    resp = tapp.get('/doc1a')
    assert resp.headers.get('Link', None) is None


def test_push_doc1b_s(tapp):
    resp = tapp.get('/doc1b')
    resp = tapp.get('/doc1b')
    assert resp.headers.get('Link', None) is None


def test_push_doc2_s(tapp):
    resp = tapp.get('/doc2')
    resp = tapp.get('/doc2')
    assert resp.headers.get('Link', None) is None

