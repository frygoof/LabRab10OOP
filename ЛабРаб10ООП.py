# Задание 1
# class Car:
#     def go(self):
#         print("The car is moving!")
# my_car = Car()
# my_car.go()
# Задание 2
# class Book:
#     def init(self, title, author, publisher):
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#
#     def get_title(self):
#         return self.title
#
#     def get_author(self):
#         return self.author
#
#     def get_publisher(self):
#         return self.publisher
#
#     def set_title(self, new_title):
#         self.title = new_title
#
#     def set_author(self, new_author):
#         self.author = new_author
#
#     def set_publisher(self, new_publisher):
#         self.publisher = new_publisher
#
#     def str(self):
#         return f"Title: {self.title}, Author: {self.author}, Publisher: {self.publisher}"
# Задание 3
# class Account:
#     def init(self, balance=0, interest_rate=0):
#         self.balance = balance
#         self.interest_rate = interest_rate / 100
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("колво")
#
#     def calculate_interest(self):
#         return self.balance * self.interest_rate
#
# my_account = Account(balance=1000, interest_rate=1.5)
#
# my_account.deposit(500)
# my_account.withdraw(200)
#
# interest_earned = my_account.calculate_interest()
#
# print(f"бал: {my_account.balance}")
# print(f"зар: {interest_earned}")
# Задание 4
# class Pet:
#     def init(self, name="", animal_type="", age=0):
#         self._name = name
#         self._animal_type = animal_type
#         self._age = age
#
#     def get_name(self):
#         return self._name
#
#     def get_animal_type(self):
#         return self._animal_type
#
#     def get_age(self):
#         return self._age
#
# pet = Pet(
#     input("Введите имя вашего домашнего животного: "),
#     input("Введите тип вашего домашнего животного: "),
#     int(input("Введите возраст вашего домашнего животного: "))
# )
#
# print(f"Имя: {pet.get_name()}")
# print(f"Тип: {pet.get_animal_type()}")
# print(f"Возраст: {pet.get_age()} лет")
# Задание 5
# class Car:
#     def init(self, year_model, make):
#         self._year_model = year_model
#         self._make = make
#         self._speed = 0
#
#     def accelerate(self):
#         self._speed += 5
#
#     def brake(self):
#         self._speed -= 5
#
#     def get_speed(self):
#         return self._speed
#
# car = Car(2022, "SomeMake")
#
# for _ in range(5):
#     car.accelerate()
#     print("Текущая скорость:", car.get_speed())
#
# for _ in range(5):
#     car.brake()
#     print("Текущая скорость:", car.get_speed())
# Задание 6
# class PersonalInformation:
#     def init(self, name, address, age, phone_number):
#         self.name = name
#         self.address = address
#         self.age = age
#         self.phone_number = phone_number
#
# my_info = PersonalInformation("Ваше Имя", "Ваш Адрес", 25, "Ваш Номер Телефона")
# friend1_info = PersonalInformation("Имя Друга 1", "Адрес Друга 1", 30, "Номер Телефона Друга 1")
# friend2_info = PersonalInformation("Имя Друга 2", "Адрес Друга 2", 28, "Номер Телефона Друга 2")
#
# print("Моя информация:")
# print("Имя:", my_info.name)
# print("Адрес:", my_info.address)
# print("Возраст:", my_info.age)
# print("Телефонный номер:", my_info.phone_number)
#
# print("\nИнформация о друге 1:")
# print("Имя:", friend1_info.name)
# print("Адрес:", friend1_info.address)
# print("Возраст:", friend1_info.age)
# print("Телефонный номер:", friend1_info.phone_number)
#
# print("\nИнформация о друге 2:")
# print("Имя:", friend2_info.name)
# print("Адрес:", friend2_info.address)
# print("Возраст:", friend2_info.age)
# print("Телефонный номер:", friend2_info.phone_number)
# Задание 7
# class Employee:
#     def init(self, name, employee_id, department, position):
#         self.name = name
#         self.employee_id = employee_id
#         self.department = department
#         self.position = position
#
#     def display_info(self):
#         print(f"Имя: {self.name}")
#         print(f"Идентификационный номер: {self.employee_id}")
#         print(f"Отдел: {self.department}")
#         print(f"Должность: {self.position}")
#         print("\n")
#
# employee1 = Employee("Сьюзан Мейерс", 47899, "Бухгалтерия", "Вице-президент")
# employee2 = Employee("Марк Джоунс", 39119, "ИТ", "Программист")
# employee3 = Employee("Джой Роджерс", 81774, "Производственный", "Инженер")
#
# employee1.display_info()
# employee2.display_info()
# employee3.display_info()
# Задание 8
# class RetailItem:
#     def init(self, description, units_in_stock, price):
#         self.description = description
#         self.units_in_stock = units_in_stock
#         self.price = price
#
#     def display_info(self):
#         print(f"Description: {self.description}")
#         print(f"Units in Stock: {self.units_in_stock}")
#         print(f"Price: ${self.price:.2f}")
#         print()
#
# item1 = RetailItem("Пиджак", 12, 59.95)
# item2 = RetailItem("Дизайнерские джинсы", 40, 34.95)
# item3 = RetailItem("Рубашка", 20, 24.95)
#
# print("Товар № 1:")
# item1.display_info()
#
# print("Товар № 2:")
# item2.display_info()
#
# print("Товар № 3:")
# item3.display_info()
# Задание 9
# class Patient:
#     def init(self, first_name, middle_name, last_name, address, city, region, postal_code, phone_number, emergency_contact_name, emergency_contact_phone):
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.last_name = last_name
#         self.address = address
#         self.city = city
#         self.region = region
#         self.postal_code = postal_code
#         self.phone_number = phone_number
#         self.emergency_contact_name = emergency_contact_name
#         self.emergency_contact_phone = emergency_contact_phone
#
#     def get_full_name(self):
#         return f"{self.first_name} {self.middle_name} {self.last_name}"
#
# class Procedure:
#     def init(self, procedure_name, procedure_date, doctor_name, procedure_cost):
#         self.procedure_name = procedure_name
#         self.procedure_date = procedure_date
#         self.doctor_name = doctor_name
#         self.procedure_cost = procedure_cost
#
# patient_instance = Patient("John", "", "Smith", "123 Main St", "Anytown", "State", "12345", "555-1234", "Emergency Contact", "555-5678")
#
# procedure1 = Procedure("Врачебный осмотр", "Сегодня", "Ирвин", 250.00)
# procedure2 = Procedure("Рентгеноскопия", "Сегодня", "Джемисон", 500.00)
# procedure3 = Procedure("Анализ крови", "Сегодня", "Смит", 200.00)
#
# print("Patient Information:")
# print("Name:", patient_instance.get_full_name())
# print("Address:", patient_instance.address)
# print("Phone:", patient_instance.phone_number)
#
# print("\nProcedure 1 Information:")
# print("Procedure:", procedure1.procedure_name)
# print("Date:", procedure1.procedure_date)
# print("Doctor:", procedure1.doctor_name)
# print("Cost:", procedure1.procedure_cost)
#
# print("\nProcedure 2 Information:")
# print("Procedure:", procedure2.procedure_name)
# print("Date:", procedure2.procedure_date)
# print("Doctor:", procedure2.doctor_name)
# print("Cost:", procedure2.procedure_cost)
#
# print("\nProcedure 3 Information:")
# print("Procedure:", procedure3.procedure_name)
# print("Date:", procedure3.procedure_date)
# print("Doctor:", procedure3.doctor_name)
# print("Cost:", procedure3.procedure_cost)
#
# total_cost = procedure1.procedure_cost + procedure2.procedure_cost + procedure3.procedure_cost
# print("\nTotal Cost of Procedures:", total_cost)
# Задание 10
# class RetailItem:
#     def init(self, description, units, price):
#         self.description = description
#         self.__units = units
#         self.__price = price
#
#     def get_description(self):
#         return self.__description
#
#     def get_units(self):
#         return self.__units
#
#     def get_price(self):
#         return self.__price
#
#
# class CashRegister:
#     def __init(self):
#         self.item_list = []
#
#     def purchase_item(self, retail_item):
#         self.__item_list.append(retail_item)
#
#     def get_total(self):
#         total = 0
#         for item in self.__item_list:
#             total += item.get_price()
#         return total
#
#     def show_items(self):
#         for item in self.__item_list:
#             print(f"Description: {item.get_description()}, Units: {item.get_units()}, Price: ${item.get_price()}")
#
#     def clear(self):
#         self.__item_list = []
#
# def main():
#     register = CashRegister()
#
#     while True:
#         print("\n1. Добавить товар в корзину")
#         print("2. Просмотреть товары в корзине")
#         print("3. Получить общую стоимость")
#         print("4. Очистить корзину")
#         print("5. Оформить заказ и выйти")
#
#         choice = input("Введите ваш выбор (1-5): ")
#
#         if choice == "1":
#             description = input("Введите описание товара: ")
#             units = int(input("Введите количество единиц товара: "))
#             price = float(input("Введите цену за единицу товара: "))
#             item = RetailItem(description, units, price)
#             register.purchase_item(item)
#             print("Товар добавлен в корзину.")
#
#         elif choice == "2":
#             print("\nТовары в корзине:")
#             register.show_items()
#
#         elif choice == "3":
#             total_cost = register.get_total()
#             print(f"\nОбщая стоимость товаров в корзине: ${total_cost:.2f}")
#
#         elif choice == "4":
#             register.clear()
#             print("Корзина очищена.")
#
#         elif choice == "5":
#             print("\nТовары в корзине:")
#             register.show_items()
#             total_cost = register.get_total()
#             print(f"Общая стоимость: ${total_cost:.2f}")
#             print("Спасибо за покупки. Завершение программы.")
#             break
#
#         else:
#             print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")
#
# if __name == "main":
#     main()
# Задание 11
# class Question:
#     def init(self, text, options, correct_option):
#         self.text = text
#         self.options = options
#         self.correct_option = correct_option
#
#     def ask_question(self):
#         print(self.text)
#         for i, option in enumerate(self.options, 1):
#             print(f"{i}. {option}")
#
#         user_answer = int(input("Ваш ответ (1-4): "))
#         return user_answer == self.correct_option
#
#
# class QuizGame:
#     def init(self, questions):
#         self.questions = questions
#         self.player1_score = 0
#         self.player2_score = 0
#
#     def play_quiz(self):
#         for question in self.questions:
#             if question.ask_question():
#                 self.player1_score += 1
#             if question.ask_question():
#                 self.player2_score += 1
#
#         print("\nВикторина завершена!\n")
#         print(f"Счет игрока 1: {self.player1_score}")
#         print(f"Счет игрока 2: {self.player2_score}")
#
#         if self.player1_score > self.player2_score:
#             print("Игрок 1 побеждает!")
#         elif self.player2_score > self.player1_score:
#             print("Игрок 2 побеждает!")
#         else:
#             print("Ничья!")
#
#