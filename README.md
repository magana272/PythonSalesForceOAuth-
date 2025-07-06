# Salesforce OAuth2 Integration in Python

This project demonstrates how to authenticate with the Salesforce REST API using OAuth2 and retrieve account information using a Python script.

---

## Features

- OAuth2 login with Salesforce
- Secure credential management using `salesforceconfig.ini`
- Queries Salesforce account data (Name, ID, Billing Address)
- Modular and object-oriented structure

---

## Requirements

- Python 3.x
- `requests` module
- A valid Salesforce Developer account with API access

---

## Installation

1. Clone the repository or copy the script into your project directory.

2. Install required Python dependencies:

    ```bash
    pip install requests
    ```

3. Create a configuration file named `salesforceconfig.ini` in the root directory with the following contents:

    ```ini
    [OAUTH]
    username = your_salesforce_username
    password = your_salesforce_password
    security_token = your_salesforce_security_token
    grant_type = password
    client_id = your_salesforce_client_id
    client_secret = your_salesforce_client_secret
    base_url = https://login.salesforce.com
    ```

    > **Important:** Never commit your `salesforceconfig.ini` file to version control. It contains sensitive credentials.

---

## Usage

Run the script using:


```bash
python salesforce_solution.py
```

## Code Structure
Class: OAuth2
| Method               | Description                                     |
| -------------------- | ----------------------------------------------- |
| `__init__()`         | Initializes the class and sets up configuration |
| `__setup__()`        | Loads credentials from `salesforceconfig.ini`   |
| `login()`            | Sends POST request to obtain access token       |
| `get_account_info()` | Uses access token to retrieve account info      |



## Main Functions
```python

class OAuth2:

    ...

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

    ...

    def get_account_info(self):
        # If token is present get out account data
        if("access_token" in self.config["OAUTH"]):
            headers = {"Authorization": "Bearer"+ " " + self.config.get("OAUTH","access_token")}
            endpoint = "/services/data/v55.0/query/?q=SELECT+NAME+,+ID+,+BillingAddress+FROM+ACCOUNT"
            response = requests.get(self.base_url+endpoint, headers = headers)
            return response.content


```
