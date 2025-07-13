class Person:
    name = "Tarek"
    @classmethod
    def person_name(cls):
        print(f"person name is {cls.name}")

Person.person_name()