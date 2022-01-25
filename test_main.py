import pytest
from main import create_app
from sqlalchemy import create_engine, text
import config

TEST_CONFIG = {
    'TESTING': True,
    'DB_URL': config.TEST_DB_URL
}


def db_file(db, filename):
    sql_lines = []
    with open(filename, 'r') as file_data:
        sql_lines = [line.strip('\n') for line in file_data if not line.startswith('--') and line.strip('\n')]

        with db.connect() as conn:
            sql_command = ''
            for line in sql_lines:
                sql_command += line
                if sql_command.endswith(';'):
                    try:
                        conn.execute(text(sql_command))
                    except Exception as e:
                        print('Fail DB Reset!!')
                        print(e)
                        return False
                    finally:
                        sql_command = ''
    return True


@pytest.fixture(scope='session')
def app():
    app = create_app(TEST_CONFIG)
    return app


@pytest.fixture(scope='session')
def db():
    db = create_engine(TEST_CONFIG['DB_URL'], encoding='utf-8', max_overflow=0)
    return db


@pytest.fixture
def client(app, db):
    db_file(db, 'test.sql')
    client = app.test_client()
    return client


def test_get_user(client):
    response = client.get('/user')
    assert response.status_code == 200
    assert response.json == {'users': [{'id': 1, 'name': 'user1'}]}
