import requests
import json
import random

#NYOOOOOOOOOOOM

get_url = 'http://localhost:3000'
post_url = 'http://localhost:4000'

get_headers = {'Content-Type': 'application/json'}
post_headers = {'Content-Type': 'application/json'}

while True:
    movement_list = [-1,0,1]
    rot_list = [-1,0,1]
    fire_list = [0,1]


    m = random.choice(movement_list)
    r = random.choice(rot_list)
    f = random.choice(fire_list)


    data = {"m":m,"r":r,"f":f}
    data = json.dumps(data)
    response = requests.post(post_url,data = data,headers = post_headers)
