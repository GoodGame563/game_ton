from models import GameState, SnakeRequest
import requests

import json

token = '0bf8a4c7-3f4d-4ed3-8749-f52054c66bfa'

server_url = 'https://games-test.datsteam.dev/play/snake3d'

api = '/player/move'

url = f"{server_url}{api}"


headers = {
    'X-Auth-Token': token,
    'Content-Type': 'application/json'
}

url = "https://games-test.datsteam.dev/play/snake3d/player/move"

# response = requests.post(url, headers=headers, json=data)

# with open('example_response.json', 'w') as file:
#     file.write(response.text)

def get_map(): 
    data = {
        'snakes': []
    }
    response = requests.post(url, headers=headers, json=data)
    return GameState(**response.json())

def move_snakes(snakes: SnakeRequest):
    response = requests.post(url, headers=headers, json=snakes.model_dump_json())
    return GameState(**response.json())

