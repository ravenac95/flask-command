from setuptools import setup, find_packages

VERSION = '0.0.3'

LONG_DESCRIPTION = open('README.rst').read()

setup(name='flask-command',
    version=VERSION,
    description="flask-command - Run you flask+gunicorn app as a command",
    long_description=LONG_DESCRIPTION,
    keywords='',
    author='Reuven V. Gonzales',
    author_email='reuven@tobetter.us',
    url="https://github.com/ravenac95/flask-command",
    license='MIT',
    platforms='*nix',
    py_modules=['flaskcommand'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'gunicorn',
        'flask',
    ],
    entry_points={},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
)
