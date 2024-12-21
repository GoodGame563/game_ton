from models import GameState, SnakeRequest
import requests
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
        "snakes": []
    }
    response = requests.post(url, headers=headers, json=data)
    try:
        result = GameState(**response.json())
        return result
    except Exception as e:
        # print(f"Error: {e}")
        return None
   

def move_snakes(snakes: SnakeRequest):
    
    data ={
        "snakes": [snake.dict() for snake in snakes.snakes]
    }
    response = requests.post(url, headers=headers, json=data)
    return GameState(**response.json())

