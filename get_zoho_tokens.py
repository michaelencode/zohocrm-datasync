import requests
import webbrowser
from flask import Flask, request
from dotenv import load_dotenv
import os

#load the .env file
load_dotenv()
client_id = os.environ.get("client_id")
client_secret = os.environ.get("client_secret")
redirect_uri = os.environ.get("redirect_uri")

app = Flask(__name__)
# Generate the authorization URL
auth_url = f'https://accounts.zoho.com/oauth/v2/auth?scope=ZohoCRM.modules.ALL,ZohoCRM.settings.ALL&client_id={client_id}&response_type=code&access_type=offline&redirect_uri={redirect_uri}'

# Open the authorization URL in the default web browser
webbrowser.open(auth_url)


@app.route('/')
def oauth_callback():
    authorization_code = request.args.get('code')

    # Use the authorization code to get the access and refresh tokens
    token_url = 'https://accounts.zoho.com/oauth/v2/token'
    token_data = {
        'code': authorization_code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code',
    }

    token_response = requests.post(token_url, data=token_data)
    token_info = token_response.json()

    access_token = token_info['access_token']
    refresh_token = token_info['refresh_token']
    print('Access Token:', access_token)
    print('Refresh Token:', refresh_token)

    return 'Access Token and Refresh Token have been printed in the console.'


if __name__ == '__main__':
    app.run(port=8000)
