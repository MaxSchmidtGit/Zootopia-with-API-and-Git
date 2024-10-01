import requests

API_KEY = 'QCXWtDYvryl2ytjklcOs0A==BKYy3Y6UCyXIpnVc'
API_URL = 'https://api.api-ninjas.com/v1/animals?name='

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
    response = requests.get(f"{API_URL}{animal_name}", headers={'X-Api-Key': API_KEY})
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return []

