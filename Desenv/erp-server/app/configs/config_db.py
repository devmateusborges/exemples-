from flask_sqlalchemy import SQLAlchemy

# ======


def configure(app):
    print(">>>Init DB")
    db = SQLAlchemy(app=app)
    db.init_app(app)
    app.db = db
    return db
