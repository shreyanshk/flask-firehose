from flask import g, session


class Connector(object):

    @staticmethod
    def get_pushed():
        """Returns a set of items that have been already pushed to client.

        Returns
        -------
        set
            Set of items that are pushed.

        """
        pushed_items = session.get("h2-pushed", None)
        if pushed_items:
            return set(pushed_items.split(','))
        else:
            return set()

    @staticmethod
    def set_pushed(inset):
        """Update client state after pushing more items at the end of request.

        Parameters
        ----------
        inset : set
            A set of URLs of pushed items.
        """
        val = ','.join(inset)
        session["h2-pushed"] = val


def push(url, *args, **kwargs):
    """Pushes the resource at given URL.

    Keyword arguments are added to the header and then positional arguments.

    Parameters
    ----------
    args : tuple
        positional arguments to append to header.
    kwargs : dict
        keyword arguments to append to header.

    Returns
    -------
    str
        The url is returned back as-is.
    """
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

    def set_header(self, resp):
        if g.get('firehose_header_val'):
            resp.headers['Link'] = g.get('firehose_header_val')
            self.connector.set_pushed(g.get('firehose_pushed_items'))
        return resp

    def init_app(self, app):
        app.before_request(self.populate)
        app.jinja_env.globals.update(push=push)
        app.after_request(self.set_header)
