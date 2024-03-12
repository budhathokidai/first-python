class Car:
    def __init__(self, brand, model):

        self.__brand = brand  # Privare attribute  
        self.__model = model

    def __drive(self):  # private method
        print("Car is driving.")

    def get_info(self):  # public method
        self.__drive()
        return f"Brand: {self.__brand}, Model: {self.__model}"

        # Creating objects of the Car class


obj = Car("Tata somu", "splender")
print(obj.get_info())
