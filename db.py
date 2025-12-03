from flask_sqlalchemy import SQLAlchemy


#To prevent circular import I made this DB file and placed the object alone so my other files
# can import from it and use the object

db = SQLAlchemy()# This creates my db object — which is an instance of SQLAlchemy



