import requests
import re
import json
import datetime


class Login():
    # defining CONSTANTS for xyz credentials
    CLIENT_ID = 'XXXXXXXXXXXXXXXX'
    CLIENT_SECRET = 'XXXXXXXXXXXXXXXX'
    USER = 'xxxxxxx'
    PASS = 'xxxxxxxxxxxx'
    URL = 'https://auth.xyz.com/oauth/authorize?client_id='

    # defining global variables
    today = datetime.datetime.now()
    today_morning = today.strftime('%Y%m%d') + "000000"
    today_evening = today.strftime('%Y%m%d') + "235959"

    # create url that gets forwarded to the token_url
    def get_login(self):
        get_auth_code = ("{}{}&response_type=code&action=Login&username={}&password={}",URL)
        # url that includes the token
        auth_code_url = requests.get(get_auth_code).url
        # extract token from token_url
        auth_code = re.search('code=(.*)&', auth_code_url).group(1)

        # get an access token
        get_access_token = "https://auth.xyz.com/oauth/token?grant_type=authorization_code&code={}&client_id={}&client_secret={}".format(auth_code,CLIENT_ID, CLIENT_SECRET)
        access_token = json.loads(requests.post(get_access_token).text)

        login_url = "https://rest.xyz.com/rest-services/login?version=*&access_token=" + access_token["access_token"]
        # capture RestToken & restUrl
        rest_credentials = json.loads(requests.get(login_url).text)
        print(rest_credentials)

    def __init__(self):
        get_login(self)