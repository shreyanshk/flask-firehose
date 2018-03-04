# Flask-Firehose

HTTP/2 Server Push for your Flask apps.


Pull requests are welcome.

## Usage
### Initialization
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


### Pushing resources
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


### Tracking pushed resources
Ideally, resources already pushed during a session shouldn't be pushed again. So, Flask-Firehose includes a simple utility class to track pushed resources using session variable 'h2-pushed'.
Additionally, Flask-Firehose also support for using custom code to track pushed resources in case the default implementation is unsuitable.

.. code-block:: python

	class Custom_connector():

		def get_pushed(self):
			"""return: type Set"""
			# your code here

		def set_pushed(self, set_of_resources_pushed):
			"""return: None"""
			# your code here


Using custom connector with Firehose

.. code-block:: python
	firehose = Firehose(connector=Custom_connector())
	firehose.init_app(app)


## Configure NGINX

```
    location = /myapp {
        proxy_pass http://upstream;
        http2_push_preload on;
    }
```

Read more at: [https://www.nginx.com/blog/nginx-1-13-9-http2-server-push/](https://www.nginx.com/blog/nginx-1-13-9-http2-server-push/)

