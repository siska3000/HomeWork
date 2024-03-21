from film_api import SWApi
from print_film_info import print_film_info, numbersers


api_client = SWApi()
film = api_client.get_film(numbersers)


print_film_info(film)