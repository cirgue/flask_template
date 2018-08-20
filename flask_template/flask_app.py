
from flask import Flask, render_template
from flask_template import db_interface as dbi
app = Flask(__name__)


@app.route("/")
def hello():
    print('grabbing user')
    user = dbi.grab_a_user()
    print('user: %s'%user['name'])
    return render_template('homepage.html', user=user)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

