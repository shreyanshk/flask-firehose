Flask-Firehose
==============

HTTP/2 Server Push for your Flask apps.


Usage
-----
Initialization
~~~~~~~~~~~~~~
With application factories

.. code-block:: python

    firehose = Firehose()

    def create_app():
        app = Flask(__name__)
        firehose.init_app(app)
        return app


Direct initialization

.. code-block:: python

    app = Flask(__name__)
    Firehose(app)


Pushing resources
~~~~~~~~~~~~~~~~~
Let the document writer decide what to push

.. code-block:: jinja

    {% extends 'base.html' %}
    {% block body %}
        <link rel="stylesheet" href="{{ push('/static/css/main.css', as='style', rel='preload') }}">
        This is some document.
    {% endblock %}


Let the backend developer decide what to push

.. code-block:: python

    from flask_firehose import push

    @app.route('/someroute')
    def render_someroute():
        push('/static/css/main.css', as='style', rel='preload')
        return render_template('some_template')


Tracking pushed resources
~~~~~~~~~~~~~~~~~~~~~~~~~
Ideally, resources already pushed during a session shouldn't be pushed again. So, Flask-Firehose includes a simple utility class to track pushed resources using session variable 'h2-pushed'.
Additionally, Flask-Firehose also supports add custom code to track pushed resources in case the default implementation is unsuitable.

.. code-block:: python

    class Custom_connector():

        def get_pushed(self):
            """Returns a set of items that have been already pushed to client.

            Returns
            -------
            set
                Set of items that are pushed.

            """
            # your code here

        def set_pushed(self, inset):
            """Update client state after pushing more items at the end of request.

            Parameters
            ----------
            inset : set
                A set of URLs of pushed items.
            """
            # your code here


Using custom connector with Firehose

.. code-block:: python

    firehose = Firehose(connector=Custom_connector())
    firehose.init_app(app)


Configure NGINX
---------------

.. code-block:: nginx

    location = /myapp {
        proxy_pass http://upstream;
        http2_push_preload on;
    }


Read more at: https://www.nginx.com/blog/nginx-1-13-9-http2-server-push/


Testing
-------
To initialize a development environment in ./venv:

.. code-block:: bash

    make devenv

To run unit tests:

.. code-block:: bash

    make test

To run integration testing with NGINX with docker:

.. code-block:: bash

    make dockertest

