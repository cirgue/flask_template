import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import config as cfg

def dlog(string):
    delim = ' | '
    logstring = delim.join([str(getframeinfo(currentframe()).lineno), str(datetime.now()), str(string)+'\n'])

    with open(cfg.logpath, 'a') as outfile:
        outfile.write(logstring)

def clean(t):
    return t.encode('ascii', 'ignore').decode()

def get_sql(filename):
    with open('sql/'+filename) as infile:
        return infile.read()

def get_dev_data(filename):
    with open('dev_data/'+filename) as infile:
        return infile.read()

def esc_string(instring):
    return "%s%s%s"%(cfg.escape_token, instring,cfg.escape_token)


def create_db():
    con = psycopg2.connect(dbname='postgres',
          user=cfg.username, host='',
          password=cfg.password)

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute("CREATE DATABASE %s  ;" % cfg.application_db)

def ex_statement(statement):
    '''
    LOGIC
    Executes SQL statement to application DB

    PARAMETERS
    statement{string} - sql statement in postgres SQL d

    RETURNS
    Nothing
    '''
    with psycopg2.connect(dbname= cfg.application_db,
        user=cfg.username, host='',
        password=cfg.password) as con:

        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        cur.execute(statement)

def ex_query(query, colnames=False, asdict=False):
    '''
    LOGIC
    Executes SQL query against application DB.

    PARAMETERS
    query{string} - sql query in postgres SQL dialect
    '''
    if asdict and colnames:
        raise Exception('You have pick either colnames or asdict. You chose both. You chose wrong.')
    try:
        with psycopg2.connect(dbname= cfg.application_db,
            user=cfg.username, host='',
            password=cfg.password) as con:

            cur = con.cursor()
            cur.execute(query)
            if colnames:
                names = [tuple([desc[0] for desc in cur.description])]
                data = cur.fetchall()
                names = names + data
                return names
            elif asdict:
                names = tuple([desc[0] for desc in cur.description])
                data = cur.fetchall()
                data_dict = []
                for row in data:
                    data_dict.append({names[i]:row[i] for i in range(0, len(names))})
                return data_dict

            else:
                return cur.fetchall()
    except Exception as e:
        print(e)
        raise e

def ex_loadcsv(csv, table, sep='|', nulls = ''):

    with psycopg2.connect(dbname= cfg.application_db,
        user=cfg.username, host='',
        password=cfg.password) as con:
        cur = con.cursor()

        if sep in csv:
            with StringIO(csv) as f:
                cursor.copy_from(f, table, sep=sep, null='')
        else:
            with open(csv) as f:
                cursor.copy_from(f, table, sep=sep, null='')

def add_user(name):
    add_statement = '''
    INSERT INTO users
    (uid,
    name)
    VALUES
    DEFAULT,
    %s
    RETURNING uid;
    '''%name

def grab_a_user():
    query = '''
    select * from users
    limit 1
    '''
    return ex_query(query, asdict=True)















