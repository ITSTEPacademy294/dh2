class Student:
    def __init__(self, name):
        self.name = name
        self.money = 500
        self.energy = 100
        self.knowledge = 0

    def study(self):
        if self.energy >= 20:
            self.knowledge += 20
            self.energy -= 20
            print("Ти повчився! +20 знань")
        else:
            print("Потрібно відпочити!")

    def work(self):
        self.money += 300
        self.energy -= 30
        print("Ти заробив 300 грн!")

    def rest(self):
        if self.money >= 100:
            self.money -= 100
            self.energy = 100
            print("Ти відпочив! -100 грн")
        else:
            print("Недостатньо грошей!")

    def status(self):
        print("Ім'я:", self.name)
        print("Гроші:", self.money)
        print("Енергія:", self.energy)
        print("Знання:", self.knowledge)


student = Student(input("Ім'я студента: "))

while True:
    print("\n1 - Навчатися")
    print("2 - Працювати")
    print("3 - Відпочити")
    print("4 - Стан студента")
    print("5 - Вийти")

    choice = input("Твій вибір: ")

    if choice == "1":
        student.study()
    elif choice == "2":
        student.work()
    elif choice == "3":
        student.rest()
    elif choice == "4":
        student.status()
    elif choice == "5":
        break
    else:
        print("Неправильний вибір!")
