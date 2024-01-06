from authlib.integrations.flask_client import OAuth

from app.env import AUTH_GOOGLE_CLIENT_ID, AUTH_GOOGLE_CLIENT_SECRET


# ======


def configure(app):
    print(">>>Init AUTH_SOCIAL")
    auth_app = OAuth(app)
    # ==============================
    auth_google = auth_app.register(
        name="google",
        client_id=AUTH_GOOGLE_CLIENT_ID,
        client_secret=AUTH_GOOGLE_CLIENT_SECRET,
        server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
        client_kwargs={"scope": "openid email profile"},
    )
    auth_client_google = auth_app.create_client("google")
    app.auth_client_google = auth_client_google
