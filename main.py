import requests
import swapi

from film_api import SWApi
from print_film_info import print_film_info


api_client = SWApi()
film = api_client.get_film(1)
print_film_info(film)