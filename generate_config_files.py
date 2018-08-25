import sys
import os
# site_name = sys.argv[1]
address = 'conttact.me'

nginx_conf_name = 'flask_app_nginx_conf'
nginx_conf_contents = '''

server {{
    listen 80;
    server_name {address};

    location / {{
        include proxy_params;
        proxy_pass http://unix:{project_directory}/flask_app.sock;
    }}

    location ^~ {project_directory}/static/ {{
    alias /static/;
    }}


}}'''.format(**{'address':address, 'project_directory':os.getcwd()})

systemd_config_name = 'flask_app.service'
systemd_config_contents = '''
[Unit]
Description=Gunicorn instance to serve flask_app
After=network.target

[Service]
User=john
Group=www-data
WorkingDirectory={project_directory}/
Environment="PATH={project_directory}/flask_app_env/bin"
ExecStart={project_directory}/flask_app_env/bin/gunicorn --workers 3 --bind unix:flask_app.sock -m 007 wsgi:app


[Install]
WantedBy=multi-user.target
'''.format(**{'project_directory':os.getcwd()})

def write_config_files():
    print('writing nginx')
    with open(nginx_conf_name, 'w') as outfile:
        outfile.write(nginx_conf_contents)
    print('writing systemd')
    with open(systemd_config_name, 'w') as outfile:
        outfile.write(systemd_config_contents)

if __name__ == '__main__':
    write_config_files()
