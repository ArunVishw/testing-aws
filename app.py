from flask import Flask, Blueprint
from routes.home import home
from routes.admin import admin
from routes.db import db

app = Flask(__name__)
if app.config['ENV']=='production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

app.register_blueprint(home, url_prefix="")
app.register_blueprint(admin, url_prefix="/admin")

db.init_app(app)
db.create_all(app=app)

if __name__ == "__main__":
    app.run(debug=True)