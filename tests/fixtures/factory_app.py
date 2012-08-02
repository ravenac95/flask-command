from flaskcommand import flask_command
from flask import Flask


app = Flask(__name__)


def app_factory(config_path):
    app.config.from_pyfile(config_path)
    return app


@app.route('/')
def index():
    test_var = app.config.get('TESTVAR', 'None')
    return "hello, there, %s" % test_var


main = flask_command(factory=app_factory)


if __name__ == '__main__':
    main()
