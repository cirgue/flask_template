import os
project_directory = os.path.dirname(os.path.abspath(__file__))
application_db='conttact'
username=os.environ.get('USER')
password=''
escape_token = '$ESCSRING100920003212344$'
logpath = 'site.log'
upload_directory = 'static/images/'



if __name__ == '__main__':
    print(project_directory)