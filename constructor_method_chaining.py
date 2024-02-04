class Mobile:
    brand = 'ASUS'
    os_type = 'Android'
    location = 'Chennai'

    def __init__(self, model, specification, color, amount):
        self.model = model
        self.specification = specification
        self.color = color
        self.amount = amount

    @classmethod
    def mod_location(cls, new_location):
        cls.location = new_location

    @classmethod
    def main_details(cls):
        print(cls.brand)
        print(cls.os_type)
        print(cls.location)

    def sub_details(self):
        Mobile.main_details()
        print(self.model)
        print(self.specification)
        print(self.color)
        print(self.amount)

# Example usage
my_mobile = Mobile("Model X", "High-end", "Black", 1000)
my_mobile.sub_details()
