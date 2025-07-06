import requests 
import json 
import configparser 

class OAuth2:

    def __init__(self):
        self.__setup__()

    def __setup__(self):

        # Configure the  Outh based on config file
        self.config = configparser.ConfigParser()
        self.config.read('salesforceconfig.ini') 
        self.login_params = {
            "username" : self.config.get("OAUTH","username"),
            "password" : self.config.get("OAUTH","password") + self.config.get("OAUTH","security_token"),
            "grant_type" : self.config.get("OAUTH","grant_type"),
            "client_id" : self.config.get("OAUTH","client_id"),
            "client_secret" : self.config.get("OAUTH","client_secret")
            }
        self.base_url = self.config.get("OAUTH","base_url")
    def __set_auth_token__(self, token):
        # Once we get a access token we can set this in our config
        self.config["OAUTH"]["access_token"] = token

    def login(self):
        # Get access token: Saves in our config
        try:
            response = requests.post(self.base_url+"/services/oauth2/token", params = self.login_params)
            if(response.status_code  != 200):
                raise Exception("Request Failed")
            responseJSON = response.json()
            self.__set_auth_token__(responseJSON["access_token"]) 
        except Exception as e:
            print(e)

    def get_account_info(self):
        # If token is present get out account data
        if("access_token" in self.config["OAUTH"]):
            headers = {"Authorization": "Bearer"+ " " + self.config.get("OAUTH","access_token")}
            endpoint = "/services/data/v55.0/query/?q=SELECT+NAME+,+ID+,+BillingAddress+FROM+ACCOUNT"
            response = requests.get(self.base_url+endpoint, headers = headers)
            return response.content
                
o_auth = OAuth2()
o_auth.login()
print(o_auth.get_account_info())
