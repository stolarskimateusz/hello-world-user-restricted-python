from requests_oauthlib import OAuth2Session
import requests

BASE_URL = "https://internal-dev.api.service.nhs.uk"  # to be changed

authorization_url = f"{BASE_URL}/oauth2/authorize"  # to be checked
access_token_url = f"{BASE_URL}/oauth2/token"  # to be checked


# replace "redirect_uri" with callback url,
# which you registered during the app registration
redirect_uri = "your_callback"

# replace with your api key
client_id = "your_client_id"

# replace with your secret
client_secret = "your_client_secret"

from local_var import *

nhsd = OAuth2Session(client_id=client_id, redirect_uri=redirect_uri)
auth_url, state = nhsd.authorization_url(authorization_url)
print(f"Visit this page in your browser: {auth_url}")

callback_url = input("Paste URL you get back here: ")

nhsd.fetch_token(
    token_url=access_token_url,
    client_secret=client_secret,
    authorization_response=callback_url,
)

r = nhsd.get(f"{BASE_URL}/hello-world/hello/user")
