from flask import request, g, session


class Connector(object):

    @staticmethod
    def get_pushed():
        """docstring comes here
        """
        pushed_items = session.get("h2-pushed", None)
        if pushed_items:
            return set(pushed_items.split(','))
        else:
            return set()

    @staticmethod
    def set_pushed(inset):
        """
        """
        val = ','.join(inset)
        session["h2-pushed"] = val


class Firehose(object):

    def __init__(self, app=None, connector=Connector):
        self.connector = connector
        self.app = app
        if app is not None:
            self.init_app(app)

    def populate(self):
        pushed_items = self.connector.get_pushed()
        setattr(g, 'firehose_pushed_items', pushed_items)
        setattr(g, 'firehose_header_val', "")

    def push(self, url, *args, **kwargs):
        print("")
        pushed_items = g.get('firehose_pushed_items')
        if url not in pushed_items:
            pushed_items.add(url)
            s = "<{}>".format(url)
            for key, val in kwargs.items():
                s += "; {}={}".format(key, val)
            for item in args:
                s += "; {}".format(item)
            s += ', '
            pstr = g.get('firehose_header_val')
            pstr += s
            setattr(g, 'firehose_header_val', pstr)
        return url

    def set_header(self, resp):
        if g.get('firehose_header_val'):
            resp.headers['Link'] = g.get('firehose_header_val')
            self.connector.set_pushed(g.get('firehose_pushed_items'))
        return resp

    def init_app(self, app):
        app.before_request(self.populate)
        app.jinja_env.globals.update(push=self.push)
        app.after_request(self.set_header)
