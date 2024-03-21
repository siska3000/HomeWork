import requests


from Film import Film


class SWApi:
    def __init__(self):
        self.base_url = "https://swapi.dev/"

    def get_entity(self, entity, entity_id):
        url = f"{self.base_url}/api/{entity}/{entity_id}/"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError('Неможливо отримати дані')

    def get_film(self, film_id):
        film_dict = self.get_entity('films', film_id)
        return Film(film_dict)

