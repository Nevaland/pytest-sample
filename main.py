# https://velog.io/@gyuseok-dev/flask-test
from flask import Flask, jsonify, request
from flask.views import MethodView

from sqlalchemy import create_engine, text

import config


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    if test_config:
        app.config.update(test_config)

    db = create_engine(app.config['DB_URL'], encoding='utf-8', max_overflow=0)

    class UserListView(MethodView):
        def __init__(self, database):
            self.db = database

        def get(self):
            users = self.db.execute("SELECT * FROM users")
            return jsonify({'users': [dict(row) for row in users]}), 200

    app.add_url_rule('/user', view_func=UserListView.as_view('user', db))
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True, port=8000)
