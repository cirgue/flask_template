# Flask-Gunicorn-Nginx setup/installation script
This code is adapted from this [Digital Ocean tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04#create-a-systemd-unit-file) for setting up flask, gunicorn, and nginx on a Digital Ocean Ubuntu 16.04 droplet with Python 3.

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

This will install Python 3, nginx, gunicorn, and flask, move the config files to the correct locations, and start gunicorn/nginx. It will then set up a Lets Encrypt cert and set nginx to serve https only. You should be able to go to `http://[domain name]` in a browser and see 'Hello there'.
You should be able to drop a flask project into this directory and as long as the `wsgi.py` file is pointing to the right place, it should work. I haven't tested this yet though so ymmv.

### To reset ssh keys on local:

After rebuilding the droplet, I would occassionally get the following error when trying to ssh into the server: `Permission denied (publickey)`. This should fix most problems on OSX:

`ssh-keygen -R [SERVER IP]`

`ssh-add ~/.ssh/[PRIVATE KEY NAME]`

`ssh root@[SERVER IP]`


### TODO
- Test with dropping in other flask apps.

### FAQ

Q: Why not just use docker?

A: Some of us keep the old ways. Seriously though, setting up Flask/Gunicorn/Nginx up the 'right way' in docker is actually more complicated than bare metal. If you're just trying to show your girlfriend/boyfriend/cat some awesome new weekend project that's totally going to make billions just you wait, then docker is probably not necessary