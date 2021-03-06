import sys
import os
import getpass

address = sys.argv[1]

nginx_conf_name = 'flask_app_nginx_conf'


'''
In the string below, we're setting up the Nginx config. Note that we have to specify the location
of the 'static' directory in line 26:27 so that resources like bootstrap or any JS will be loaded
correctly.
'''
nginx_conf_contents = '''

server {{
    listen 80;
    server_name {address};

    location / {{
        include proxy_params;
        proxy_pass http://unix:{project_directory}/flask_app.sock;
    }}

    location ^~ /static/ {{
    root {project_directory}/flask_template/;
    }}


}}'''.format(**{'address':address, 'project_directory':os.getcwd()})


systemd_config_name = 'flask_app.service'
systemd_config_contents = '''
[Unit]
Description=Gunicorn instance to serve flask_app
After=network.target

[Service]
User={username}
Group=www-data
WorkingDirectory={project_directory}
Environment="PATH={project_directory}/flask_app_env/bin"
ExecStart={project_directory}/flask_app_env/bin/gunicorn --workers 3 --bind unix:flask_app.sock -m 007 wsgi:app


[Install]
WantedBy=multi-user.target
'''.format(**{'project_directory':os.getcwd(), 'username':getpass.getuser()})

def write_config_files():
    print('writing nginx')
    with open(nginx_conf_name, 'w') as outfile:
        outfile.write(nginx_conf_contents)
    print('writing systemd')
    with open(systemd_config_name, 'w') as outfile:
        outfile.write(systemd_config_contents)

if __name__ == '__main__':
    write_config_files()
