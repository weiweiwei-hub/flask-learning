from flask import Flask
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
@app.route('/index')
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
