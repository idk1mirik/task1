class info:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}")

chel1 = info("Андрей", 17)

chel1.print_info()