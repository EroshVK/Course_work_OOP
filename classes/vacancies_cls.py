class Vacancies:
    """
    Класс для работы с вакансиями
    """
    def __init__(self, title, salary, experience, description, area, link):
        self.title = title
        self.salary = salary
        self.experience = experience
        self.description = description
        self.area = area
        self.link = link

    def __str__(self):
        """
        Метод для отображения информации об объекте класса для пользователей
        """
        return f'''Вакансия: {self.title}
Зарплата: {self.salary}
Требуемый опыт: {self.experience}
Описание: {self.description}
Город: {self.area}
Ссылка: {self.link}'''

    def __ge__(self, other):
        """
        Метод для сравнения (>=) зарплат двух экземпляров класса
        """
        return self.salary >= other.salary
