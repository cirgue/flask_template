from flask_template import db_interface as dbi


def setup():
#     try:
#         print('trying to setup db')
#         dbi.create_db()
#     except Exception as e:
#         print(e)

    dbi.create_db()

    dbi.ex_statement(dbi.get_sql('create_users.sql'))
    dbi.add_user('John')

if __name__ == '__main__':
    setup()