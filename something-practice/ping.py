
import requests
from requests.exceptions import ReadTimeout
try:
    response = requests.get('https://www.github.com',timeout=0.1)
    print(response.status_code)
except ReadTimeout:
    print('timeout')