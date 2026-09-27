class Pet:
    print("Hi, I am the Pet class!")
pet_object = Pet()
class PetProfile:
    category = "pet"
    def __init__(self, name, animal_type, age, favourite_food):
        self.name = name
        self.animal_type = animal_type
        self.age = age
        self.favourite_food = favourite_food
pet1=PetProfile("Willow", "dog", 14, "biscuits")
pet2=PetProfile("Oakley", "cat", 9, "tuna")
print("Willow is a {}".format(pet1.category))
print("Oakley is a {}".format(pet2.category))
print("{} is a {} and is {} years old. She likes to eat {}.".format(pet1.name, pet1.animal_type, pet1.age, pet1.favourite_food))
print("{} is a {} and is {} years old. She likes to eat {}.".format(pet2.name, pet2.animal_type, pet2.age, pet2.favourite_food))