# Read me

## Installation
### Variables
There are two ways to set all neccessary variables.
1. Set `redirect_uri`, `client_id` and `client_secret` using environment variables, using capitalised names:
    a. for Unix-like systems:
        - for redirect_uri:
            `export REDIRECT_URI="your_uri_here"`
        - for client_id:
            `export CLIENT_ID="your_id_here"`
        - for client_secret:
            `export CLIENT_SECRET="your_secret_here"`
2. Set the variables in `local_var.py`, example configuration is in `local_var_example.py`.

### Requirements
To install requirements type:
`pip install -r requirements.txt`

## Run
after requirements are installed the app can be run with:
`python snippet.py`
