from flaskcommand import flask_command
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "hello, there"


main = flask_command(app)


if __name__ == '__main__':
    main()
