import requests
import string
import random


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


url_post = 'http://localhost:5000/post'
url_get = 'http://localhost:5000/get'

for i in range(1000):
    params = {'user': generate_random_string(6), 'message': generate_random_string(6)}
    r = requests.post(url_post, params=params)
    print(r.text, r.status_code)
    r = requests.get(url_get)
    print(r.text, r.status_code)
