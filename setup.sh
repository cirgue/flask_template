SITE_NAME=$1
sudo add-apt-repository ppa:certbot/certbot -y
sudo apt-get update
sudo apt-get install -y python3-pip python3-dev nginx python-certbot-nginx
sudo pip3 install virtualenv
virtualenv flask_app_env
source flask_app_env/bin/activate
pip install gunicorn
pip install -r requirements.txt
python generate_config_files.py $SITE_NAME
#Test that the flask app is working correctly
# sudo ufw allow 5000
# python flask_app.py

source setup_nginx.sh
source setup_systemd.sh

sudo certbot --nginx -d $SITE_NAME
sudo certbot renew --dry-run
























