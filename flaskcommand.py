import os
import sys
from gunicorn.app.base import Application


class FlaskApplication(Application):
    @classmethod
    def from_factory(cls, app_factory, proc_name=None):
        return cls(app_factory, proc_name=proc_name)

    def __init__(self, app_factory, proc_name=None):
        usage = '%prog [OPTIONS] [FLASK_CONFIG_PATH]'

        self._app_factory = app_factory
        self._proc_name = proc_name or 'flask'
        self.flask_config_path = None

        super(FlaskApplication, self).__init__(usage)

    def init(self, parser, opts, args):
        if len(args) >= 1:
            self.flask_config_path = args[0]

        self.cfg.set("default_proc_name", self._proc_name)

        sys.path.insert(0, os.getcwd())

    def load(self):
        config_path = self.flask_config_path
        config_absolute_path = config_path
        if config_path:
            config_absolute_path = os.path.abspath(config_path)
        return self._app_factory(config_absolute_path)


class FlaskCommand(object):
    def __init__(self, app_factory):
        self._app_factory = app_factory

    def __call__(self):
        gunicorn_app = FlaskApplication.from_factory(self._app_factory)
        return gunicorn_app.run()


def flask_command(app=None, factory=None, proc_name=None):
    """Creates a function that can act as an entry point for a flask app

    This allows it to be called from the command line.
    """
    if not bool(app) != bool(factory):
        raise TypeError('app or factory argument required, but not both')
    if app:
        factory = lambda config: app
    return FlaskCommand(factory)
