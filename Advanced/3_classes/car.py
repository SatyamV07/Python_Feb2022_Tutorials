class BaseModel:
    """Represent the base model of the coupe"""

    rim = "normal"  # Class Attribute
    engine_liters = 1.5  # Class Attribute

    def engine_sound(self) -> str:  # Instance Method
        return "putt putt"

    def horn_sound(self) -> str:  # Instance Method
        return "beep beep"

    def __repr__(self) -> str:
        return f"The name of the class is : {__class__.__name__}"


coupe = BaseModel()
print(coupe)
print(coupe.rim)
print(coupe.engine_liters)
print(coupe.engine_sound())
print(coupe.horn_sound())

print()


class Sport_Model(BaseModel):  # Inheritance
    """Represent the Sports model of the coupe"""

    rim = "Sport"  # Class Attribute
    engine_liters = 3  # Class Attribute

    def engine_sound(self) -> str:  # Instance Method
        return "VROOM VROOM"

    def horn_sound(self) -> str:  # Instance Method
        return "beep beep".upper()

    def __repr__(self) -> str:
        return f"The name of the class is : {__class__.__name__}"


coupe_sport = Sport_Model()
print(coupe_sport)
print(coupe_sport.rim)
print(coupe_sport.engine_liters)
print(coupe_sport.engine_sound())
print(coupe_sport.horn_sound())


class Luxury_Model(BaseModel):  # Inheritance
    """Represent the Luxury model of the coupe"""

    rim = "Luxury"

    def engine_sound(self) -> str:  # Instance Method
        return "VROOM VROOM"

    def horn_sound(self) -> str:  # Instance Method
        return "beep beep".upper()

    def __repr__(self) -> str:
        return f"The name of the class is : {__class__.__name__}"


print()
coupe_luxury = Luxury_Model()
print(coupe_luxury)
print(coupe_luxury.rim)
print(coupe_luxury.engine_liters)
print(coupe_luxury.engine_sound())
print(coupe_luxury.horn_sound())


class Luxury_Sport_Model(Luxury_Model, Sport_Model):
    def __repr__(self) -> str:
        return f"The name of the class is : {__class__.__name__}"


print()
coupe_luxury_sport = Luxury_Sport_Model()
print(coupe_luxury_sport)
print(coupe_luxury_sport.rim)
print(coupe_luxury_sport.engine_liters)
print(coupe_luxury_sport.engine_sound())
print(coupe_luxury_sport.horn_sound())


class Sport_Luxury_Model(Sport_Model, Luxury_Model):
    def __repr__(self) -> str:
        return f"The name of the class is : {__class__.__name__}"


print()
coupe_sport_luxury = Sport_Luxury_Model()
print(coupe_sport_luxury)
print(coupe_sport_luxury.rim)
print(coupe_sport_luxury.engine_liters)
print(coupe_sport_luxury.engine_sound())
print(coupe_sport_luxury.horn_sound())

print()
print(Sport_Luxury_Model.__mro__)

print()
"""Custom Attributes"""

coupe_custom = Sport_Luxury_Model()
print(f"{coupe_custom} has {coupe_custom.rim} level")
coupe_custom.rim = "custom"
print(f"{coupe_custom} has {coupe_custom.rim} level")
print()

coupe_custom.brakes = "racing"
BaseModel.brakes = "standard"
print(f"{coupe_custom} has {coupe_custom.brakes} brakes")
print(f"{BaseModel()} has {BaseModel.brakes} brakes")
