class Animal:
    def __init__(self, name: str):
        self.name = name
        self.db = AnimalDB()

    def get_name(self) -> str:
        return self.name

    def get(self, id):
        return self.db.get_animal(id)
    
    def save(self):
        self.db.save(animal=self)


###https://github.com/heykarimoff/solid.python/blob/master/1.srp.py
