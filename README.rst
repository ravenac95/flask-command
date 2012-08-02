flask-command - A tool to use a flask+gunicorn app from the command line
========================================================================

flask-command is a simple tool that allows you to call your flask application
from the command line after wrapping through gunicorn. This is useful if you'd
like to create a ``console_script`` entry point for your flask application.

Intended Use Case
-----------------

Let's assume your project is called myproject. A flask app exists or is
accessible from myproject/__init__.py. The following shows how you'd use
flask-command.

In a file called myproject/main.py::
    
    from flaskcommand import flask_command
    from myproject import app

    main = flask_command(app)

In your setup.py file::
    
    setup(name='myproject',
        version='0.0.1',
        description="myproject - is awesome",
        long_description="myproject - is really awesome",
        keywords='',
        author='Reuven V. Gonzales',
        author_email='reuven@tobetter.us',
        packages=['myproject'],
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            'flask-command',
            'flask',
        ],
        entry_points={
            'console_scripts': [
                # WITH FLASK-COMMAND YOU CAN
                # DEFINE YOUR SCRIPT HERE :-)
                'myproject-web = myproject.main:main', 
            ]
        },
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        ],
    )

Now, after installing your project you can start your flask server like this::
    
    $ myproject-web -b 127.0.0.1:8000 -w 4 some_config_path

At this time specifying a path to a configuration file is required, but this
probably won't be so in the future.
