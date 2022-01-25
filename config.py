DB = {
    'host': 'localhost',
    'user': 'root',
    'pass': '1234',
    'db': 'my_flask'
}
DB_URL = f'mysql://{DB["user"]}:{DB["pass"]}@{DB["host"]}/{DB["db"]}?charset=utf8'

TEST_DB = 'test_flask'
TEST_DB_URL = f'mysql://{DB["user"]}:{DB["pass"]}@{DB["host"]}/{TEST_DB}?charset=utf8'
