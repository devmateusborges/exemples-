from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#======
def configure(app):
    print('>>>Init DB')
    db.init_app(app)
    return db

