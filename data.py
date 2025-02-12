import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response_code = requests.get(url="https://opentdb.com/api.php", params=parameters)
response_code.raise_for_status()

data = response_code.json()
question_data = data["results"]

