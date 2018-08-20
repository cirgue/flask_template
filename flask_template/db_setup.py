import db_interface as dbi

try:
    dbi.create_db()
except Exception as e:
    print(e)


dbi.ex_statement(dbi.get_sql('create_users.sql'))
dbi.add_user('John')
