from flask_template import db_interface as dbi
import getpass

def setup():
    try:
        print('trying to setup db')
        dbi.create_db()
    except Exception as e:
        print(e)

    dbi.ex_statement(dbi.get_sql('create_users.sql'))
    print('adding user')
    dbi.add_user(getpass.getuser())
    print('successfully added user')

if __name__ == '__main__':
    setup()