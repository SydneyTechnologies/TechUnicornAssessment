# To Run this code you will need to install the following dependencies, request and cachetools
# if the repository was cloned, and python is installed, run the command
# if pipenv is installed
# pipenv install --dev on the command line, 
# else run the command pip install -r requirements.text to install the dependencies

import requests
import cachetools.func

@cachetools.func.ttl_cache(maxsize=128, ttl=300) # cache result for 5mins
def make_call():
    API = "https://www.randomuser.me/api"
    result = []
    for i in range(10):
        result.append(requests.get(API).json()["results"][0])
    return result


make_call() #calling the function