def test_for_header(tapp):
    resp = tapp.get('/')
    assert resp.headers['Link'] == '</static/css/normalize.css>; as=style; rel=preload, </static/css/main.css>; as=style; rel=preload, </static/js/vendor/modernizr-3.5.0.min.js>; rel=preload, '
