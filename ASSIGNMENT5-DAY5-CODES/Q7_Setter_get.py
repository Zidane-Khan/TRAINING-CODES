class Car:
    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year

    # Getter and Setter for 'make'
    def get_make(self):
        return self._make

    def set_make(self, make):
        self._make = make

    # Getter and Setter for 'model'
    def get_model(self):
        return self._model

    def set_model(self, model):
        self._model = model

    # Getter and Setter for 'year'
    def get_year(self):
        return self._year

    def set_year(self, year):
        self._year = year


car = Car("khn", "BMW", 1100)
print(car.get_make())  
car.set_model("AUdi")
print(car.get_model())  
