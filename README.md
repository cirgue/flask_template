# Flask-Gunicorn-Nginx setup/installation script
This code is adapted from this [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04#create-a-systemd-unit-file) for setting up flask, postgres, gunicorn, and nginx with a Let's Encrypt cert on a Digital Ocean Ubuntu 16.04 droplet with Python 3.

[Digital Ocean Let's Encrypt for Nginx](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04)


### Quickstart
SSH into the digital ocean server and run the following:

```
adduser [USERNAME]
adduser [USERNAME] sudo
cd
git clone https://github.com/cirgue/do_deploy_tutorial.git
source setup.sh [domain name]
```

After installation, you should be able to go to `http://[domain name]` in a browser and see the homepage. Currently, certbot is set up to only get a staging cert, which the browser shouldn't trust by default.

### To reset ssh keys on local:

`ssh-keygen -R [SERVER IP]`

`ssh-add ~/.ssh/[PRIVATE KEY NAME]`

`ssh root@[SERVER IP]`

