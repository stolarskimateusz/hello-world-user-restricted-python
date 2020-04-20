import os

from flask import Flask, redirect, request, session, url_for
from flask.json import jsonify
from requests_oauthlib import OAuth2Session

app = Flask(__name__)
app.secret_key = os.urandom(24)


BASE_URL = "https://internal-dev.api.service.nhs.uk"  # to be changed

authorize_url = f"{BASE_URL}/oauth2/authorize"
access_token_url = f"{BASE_URL}/oauth2/token"


# replace "redirect_uri" with callback url,
# which you registered during the app registration
redirect_uri = "your_callback"

# replace with your api key
client_id = "your_client_id"

# replace with your secret
client_secret = "your_client_secret"

from local_var import *


@app.route("/")
@app.route("/login")
def login():
    nhsd = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri)
    authorization_url, state = nhsd.authorization_url(authorize_url)

    # State is used to prevent CSRF, keep this for later.
    session["oauth_state"] = state
    return redirect(authorization_url)


@app.route("/callback", methods=["GET"])
def callback():
    nhsd = OAuth2Session(client_id, state=session["oauth_state"])
    token = nhsd.fetch_token(
        token_url=access_token_url,
        client_secret=client_secret,
        authorization_response=request.url,
    )
    session["oauth_token"] = token
    return redirect(url_for(".profile"))


@app.route("/profile", methods=["GET"])
def profile():
    # Fetching a protected resource using an OAuth 2 token.
    nhsd = OAuth2Session(client_id, token=session["oauth_token"])

    user_restricted_endpoint = jsonify(
        nhsd.get(f"{BASE_URL}/hello-world/hello/user").json()
    )

    return jsonify(nhsd.get(user_restricted_endpoint).json())


if __name__ == "__main__":
    os.environ["FLASK_ENV"] = "development"

    app.run(debug=True)
