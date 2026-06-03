# # задание 1
#
# class BankAccount:
#     def __init__(self, account_number, balans):
#         self.__account_number = account_number
#         self.__balances = balans
#
#     @property
#     def get_account_number(self):
#         return self.__account_number
#
#
#     @property
#     def get_balances(self):
#         return self.__balances
#
#     @property
#     def is_negative(self):
#         return self.__balances < 0
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balances += amount
#         else:
#             print("меньше 0")
#
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("больше 0")
#         if amount > self.__balances:
#             print("нету денег")
#         else:
#             self.__balances -= amount
#
# if __name__ == "__main__":
#     bank = BankAccount(10, 10000000)
#     print(bank.get_balances)
#     bank.deposit(10)
#     print(bank.get_balances)
#     bank.withdraw(100)
#     print(bank.get_balances)
#     print(bank.get_account_number)
#     print(bank.is_negative)
#
#
#
# # задание 2
#
# class Vehicle:
#     def __init__(self, brand = "", model= "", year = "1999"):
#         self._model = model
#         self._brand = brand
#         self._year = year
#
#
#     def info(self):
#         return f"brand: {self._brand}, model: {self._model}, year: {self._year}"
#
#     def start_engine(self):
#         return "Двигатель запущен"
#
# class Car(Vehicle):
#     def __init__(self, brand = "", model= "", year = "1999", number_of_doors = 0):
#         super().__init__(brand, model, year)
#         self._number_of_doors = number_of_doors
#
#     def info(self):
#         return f"brand: {self._brand}, model: {self._model}, year: {self._year}, number_of_doors: {self._number_of_doors}"
#
# class Motorcycle(Vehicle):
#     def __init__(self, brand = "", model= "", year = "1999", has_sidecar = False):
#         super().__init__(model, brand, year)
#         self._has_sidecar = has_sidecar
#
#     def start_engine(self):
#         return "Рокот мотоцикла"
#
#
# d = Vehicle()
# print(d.start_engine())
# print(d.info())
#
# p = Motorcycle()
# print(p.start_engine())
# print(p.info())
#
# c = Car()
# print(c.start_engine())
# print(c.info())


# задание 3

# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#
#     def __str__(self):
#         return f'{self.name} {self.age} {self.grade}'
#
#     def __repr__(self):
#         return f'{self.name} {self.age} {self.grade}'
#
# d = Student(12, 12 , 12)
# print(d)



# задание 4

#
# class Library:
#     def __init__(self):
#         self._books = {}
#
#     def __setitem__(self, title, auter):
#         self._books[title] = auter
#
#     def __getitem__(self, title):
#         return self._books.get(title, "Неть тякой книги :)")
#
#     def __len__(self):
#         return len(self._books)
#
#     def __call__(self):
#         return list(self._books.keys())
#
#
# lib = Library()
#
# lib["="] = "перерождение в ленина"
# lib["мимикью"] = "Тразин"
# 
# print(lib)
# print(lib["="])
# print(lib["мимикью"])