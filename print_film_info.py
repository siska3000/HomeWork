import requests
from film_api import SWApi


numbersers = int(input("Введіть ідентифікатор фільму: "))


def fetch_data(url):
    recponse = requests.get(url)
    if recponse.status_code == 200:
        return recponse.json()
    else:
        raise ValueError('Неможливо отримати дані')


def get_name_from_url(url):
    data = fetch_data(url)
    return data["name"]


def print_film_info(film):
    print(f"Фільм: {film.title}")
    print("Персонажі:")
    for i, character_url in enumerate(film.characters, numbersers):
        character_name = get_name_from_url(character_url)
        print(f"  {i}. {character_name}")

    print("Транспортні засоби:")
    for i, vehicle_url in enumerate(film.vehicles, numbersers):
        vehicle_name = get_name_from_url(vehicle_url)
        print(f"  {i}. {vehicle_name}")

    print("Космічні кораблі:")
    for i, starship_url in enumerate(film.starships, numbersers):
        starship_name = get_name_from_url(starship_url)
        print(f"  {i}. {starship_name}")

    print("Види істот:")
    for i, species_url in enumerate(film.species, numbersers):
        species_name = get_name_from_url(species_url)
        print(f"  {i}. {species_name}")
