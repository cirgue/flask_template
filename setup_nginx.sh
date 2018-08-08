sudo mv flask_app_nginx_conf /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/flask_app_nginx_conf /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
sudo ufw delete allow 'Nginx HTTP'
