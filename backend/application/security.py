from flask_security import Security, SQLAlchemyUserDatastore
from .data.model import db, User, Role

user_datastore = SQLAlchemyUserDatastore(db,User,Role)
security = Security()