from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)

mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dev'
app.config['MYSQL_PASSWORD'] = 'kP_^zZ99uuSE+}$7'
app.config['MYSQL_DB'] = 'soups'

from souptime import souptime as souptime_blueprint
app.register_blueprint(souptime_blueprint)

import logging
handler = logging.FileHandler("/home/dev/souptime/app.log")
handler.setLevel(logging.ERROR)
app.logger.addHandler(handler)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
