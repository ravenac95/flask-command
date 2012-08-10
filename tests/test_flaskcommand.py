import os
import requests
import subprocess
import textwrap
import random
import time
from tests import fixtures_path


class TestUsingSimpleApp(object):
    def connect(self):
        # FIXME need to find a better way to open a random port
        app_path = fixtures_path('simple_app.py')
        self.app = subprocess.Popen(['python', app_path, '-b',
            '127.0.0.1:14444'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(5)

    def disconnect(self):
        self.app.terminate()

    def test_request(self):
        self.connect()
        try:
            response = requests.get('http://127.0.0.1:14444/')
        finally:
            self.disconnect()
        assert response.text == 'hello, there'


class TestUsingAppWithFactory(object):
    def setup(self):
        self.config_path = fixtures_path('config.py')
        config_file = open(self.config_path, 'w')

        self.random_string = random.choice('abcdefghijklmnopqrstuvwxyz')

        config_file.write(textwrap.dedent("""
            TESTVAR = "%s"
        """ % self.random_string))
        config_file.close()

    def teardown(self):
        os.remove(self.config_path)

    def connect(self):
        # FIXME need to find a better way to open a random port
        app_path = fixtures_path('factory_app.py')
        self.app = subprocess.Popen(['python', app_path, '-b',
            '127.0.0.1:14444', self.config_path],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(5)

    def disconnect(self):
        self.app.terminate()
        print self.app.stdout.read()

    def test_request(self):
        self.connect()
        try:
            response = requests.get('http://127.0.0.1:14444/')
        finally:
            self.disconnect()
        assert response.text == 'hello, there, %s' % self.random_string
