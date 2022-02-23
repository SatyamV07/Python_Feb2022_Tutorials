class BaseModel_with_self:
    """Represent the base model of the car"""

    rim = "normal"  # Class Attribute
    engine_liters = 1.5  # Class Attribute

    def engine_sound(self) -> str:  # Instance Method
        return "putt putt"

    def horn_sound(self) -> str:  # Instance Method
        return "beep beep"

    def __repr__(self):
        print(f"{__class__.__name__}")


suzuki = BaseModel_with_self()
print(suzuki.rim)
print(suzuki.engine_liters)
print(suzuki.engine_sound())
print(suzuki.horn_sound())
print()


hyundai = BaseModel_with_self()
hyundai.rim = "alloy"
hyundai.engine_liters = 3
print(hyundai.rim)
print(hyundai.engine_liters)
print(hyundai.engine_sound())
print(hyundai.horn_sound())

print()
print(BaseModel_with_self.rim)
print(BaseModel_with_self.engine_liters)
print()


class BaseModel_with_instantiation:
    def __init__(self, rim, engine_liters) -> None:
        self.rim = rim
        self.engine_liters = engine_liters

    def engine_sound(self) -> str:  # Instance Method
        return "putt putt"

    def horn_sound(self) -> str:  # Instance Method
        return "beep beep"


car = BaseModel_with_instantiation("normal", 1.5)
print(car.engine_liters)
print(car.rim)
print(car.engine_sound())
print(car.horn_sound())

print()


class BaseModel_without_self:
    """Represent the base model of the car"""

    rim = "normal"  # Class Attribute
    engine_liters = 1.5  # Class Attribute

    def engine_sound() -> str:  # Instance Method
        return "putt putt"

    def horn_sound() -> str:  # Instance Method
        return "beep beep"


car = BaseModel_without_self
print(car.engine_liters)
print(car.rim)
print(car.engine_sound())
print(car.horn_sound())

print()
print(dir(BaseModel_with_self))
