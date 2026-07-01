import requests

API_KEY = 'qxnYeyzdqUCF16UH1BUTYugjvZvw9EmOAEo048O6'
URL_API = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_user):
    """Fetch animal data from the Animals API."""
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_user}
    try:
        response = requests.get(URL_API, headers=headers, params=params)
        animals_data = response.json()
        if not animals_data:
            print(f"No animals found for '{animal_user}'.")
        return animals_data
    except Exception as e:
        print(f"Error connecting to the API: {e}")
        return []
