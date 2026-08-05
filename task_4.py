class EmployeeSalary:

    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod # По заданию очень странное название метода класса. get обычно значит обычный метод который должен что-то вернуть
    # а тут создание объекта через атрибуты конструктора. Но раз такое трубется в подсказках в курсе....
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod # аналогично странное название метода класса
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
           email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.get_hours * self.hourly_payment

