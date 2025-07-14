import os
from flask_admin import Admin
from database.db import db
from models.User import User
from models.People import People
from models.Planet import Planet
from models.Favorite_People import FavoritePeople
from models.Favorite_Planet import FavoritePlanet
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Planet, db.session))
    admin.add_view(ModelView(People, db.session))
    admin.add_view(ModelView(FavoritePeople, db.session))
    admin.add_view(ModelView(FavoritePlanet, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))