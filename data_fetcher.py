import requests

API_KEY = "QCXWtDYvryl2ytjklcOs0A==BKYy3Y6UCyXIpnVc"

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    },
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {
        "X-Api-Key": API_KEY
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return []
