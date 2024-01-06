from flask_marshmallow import Marshmallow


# ======


def configure(app):
    print('>>>Init SEREALIZER')
    ma = Marshmallow()
    ma.init_app(app)
    return ma
