# Flask-Template
A Flask API template for Python 3.6+

MIT License

**NOTE:** I highly recommend using [PyCharm](https://www.jetbrains.com/pycharm/) to configure your environment. It is free for university students. PyCharm lets you easily manage virtual environments, set environment variables, and manage version control.

## Installation

Clone the Git repository into your folder of choice. Navigate to that folder in your terminal. If you are using a virtual environment, make sure you are in that environment. Then, run the following commands in your terminal:
```
pip install --upgrade pip

pip install flask

pip install flask-migrate
```

You've just installed [Flask](http://flask.pocoo.org/) and [Flask-Migrate](https://flask-migrate.readthedocs.io/)!

Next, navigate to the `app` folder (containing `Docs`, `Endpoints`, `Models`, etc) and run the following commands:
```
flask db init
flask db migrate
flask db upgrade
```

Those commands just:
1. Created a `migrations` folder
2. Created your first migrations from the models in the `Models` folder
3. Ran your migrations to create the required database/tables/columns.

Finally, navigate back to the base `Flask-Template` folder and run `main.py`. Voila!
