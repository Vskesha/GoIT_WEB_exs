import json
import requests

if __name__ == '__main__':
    data = {"name": "Test note", "description": "Testing", "done": False}
    headers = {'Content-type': 'application/json'}

    response = requests.post('http://127.0.0.1:8000/notes', data=json.dumps(data), headers=headers)

    print(response.json())
