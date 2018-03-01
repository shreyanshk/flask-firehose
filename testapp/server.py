from flask import Flask, render_template
from flask_firehose import Firehose


app = Flask(__name__)
Firehose(app)
app.config['SECRET_KEY'] = 's3cr3t k3y'


@app.route('/', methods=['GET'])
def render_root():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8086, debug=True)
