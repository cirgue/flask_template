import os
import getpass

project_directory = os.path.dirname(os.path.abspath(__file__))
application_db='flask_template_db'
username=getpass.getuser()
password=''
escape_token = '$ESCSRING100920003212344$'
logpath = 'flask_template.log'




if __name__ == '__main__':
    print(project_directory)