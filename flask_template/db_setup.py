import db_interface as dbi

dbi.create_db()
dbi.ex_statement(dbi.get_sql('create_users.sql'))
dbi.add_user('John')
