class Film:
    def __init__(self, data):
        self.title = data["title"]
        self.characters = data["characters"]
        self.vehicles = data["vehicles"]
        self.starships = data["starships"]
        self.species = data["species"]
