from flask import Flask, render_template
from flask_firehose import Firehose, push


app = Flask(__name__)
Firehose(app)
app.config['SECRET_KEY'] = 's3cr3t k3y'


@app.route('/', methods=['GET'])
def render_index():
    return render_template('index.html')


@app.route('/doc1a', methods=['GET'])
def render_doc1a():
    return render_template('doc1.html')


@app.route('/doc1b', methods=['GET'])
def render_doc1b():
    push('/static/js/vendor/modernizr-3.5.0.min.js', rel='preload')
    return render_template('doc1.html')


@app.route('/doc2', methods=['GET'])
def render_doc2():
    push('/static/js/vendor/modernizr-3.5.0.min.js', rel='preload')
    return render_template('doc2.html')


if __name__ == '__main__':
	# No need for full WSGI server to test the extension.
    app.run(host='0.0.0.0', port=8086, debug=True)
