from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstract Base Class for every person in the Smart City.
    """

    person_count = 0

    def __init__(self,
                 person_id,
                 name,
                 age,
                 gender,
                 phone,
                 address):

        Person.person_count += 1

        self._person_id = person_id
        self._name = name
        self._age = age
        self._gender = gender
        self._phone = phone
        self._address = address

    @property
    def person_id(self):
        return self._person_id

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @property
    def phone(self):
        return self._phone

    @property
    def address(self):
        return self._address

    @name.setter
    def name(self, value):
        self._name = value

    @phone.setter
    def phone(self, value):
        self._phone = value

    @address.setter
    def address(self, value):
        self._address = value

    @classmethod
    def total_people(cls):
        return cls.person_count

    @abstractmethod
    def display(self):
        pass