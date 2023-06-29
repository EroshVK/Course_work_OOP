import os.path

from classes.hh_cls import HeadHunterAPI
from classes.data_to_json import JSONHandler
from classes.sj_cls import SuperJobAPI


def choice_hh():
    """
    Метод для работы с пользователем при выборе HeadHunter
    """
    keyword = input("Введите ключевое слово для запроса: ")
    pages = int(input("Введите количество страниц вакансий (на одной странице 100 вакансий): "))

    hh = HeadHunterAPI()
    data_hh = hh.get_vacancies(keyword, pages)
    processed_vacancies_hh = hh.process_vacancies(data_hh)

    print("Вакансии HeadHunter: ")
    for item in processed_vacancies_hh:
        print(item)

    file_hh = 'vacancies_hh.json'
    if os.path.isfile(file_hh):
        os.remove(file_hh)
    hh = JSONHandler(file_hh)
    for item in processed_vacancies_hh:
        hh.add_vacancy(item)
    print("Файл с данными вакансиями сохранен")

    keyword_found = input("Введите дополнительное ключевое слово для поиска вакансий в файле (например разработчик, стажер, аналитик и т.д.): ")
    found_vacancies = hh.get_vacancy(keyword_found)
    if len(found_vacancies) > 0:
        for item in found_vacancies:
            print(item)
    else:
        print("Нет вакансий, соответствующих заданным критериям.")


def choice_sj():
    """
    Метод для работы с пользователем при выборе SuperJob
    """
    keyword = input("Введите ключевое слово для запроса: ")
    pages = int(input("Введите количество страниц вакансий (на одной странице 100 вакансий): "))

    sj = SuperJobAPI()
    data_sj = sj.get_vacancies(keyword, pages)
    processed_vacancies_sj = sj.process_vacancies(data_sj)

    print("Вакансии SuperJob: ")
    for item in processed_vacancies_sj:
        print(item)

    file_sj = 'vacancies_sj.json'
    if os.path.isfile(file_sj):
        os.remove(file_sj)
    sj = JSONHandler(file_sj)
    for item in processed_vacancies_sj:
        sj.add_vacancy(item)
    print("Файл с данными вакансиями сохранен")

    keyword_found = input(
        "Введите дополнительное ключевое слово для поиска вакансий в файле (например разработчик, стажер, аналитик и т.д.): ")
    found_vacancies = sj.get_vacancy(keyword_found)
    if len(found_vacancies) > 0:
        for item in found_vacancies:
            print(item)
    else:
        print("Нет вакансий, соответствующих заданным критериям.")


def interact_with_user():
    """
    Метод для работы с пользователем
    """
    print("Добро пожаловать! Выберите платформу для поиска вакансий:")
    print("1. HeadHunter     2. SuperJob")
    print("Для выхода нажмите 3")

    while True:
        choice = input("Выберите действие: ")

        if choice == "1":
            choice_hh()

        elif choice == "2":
            choice_sj()

        elif choice == "3":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    interact_with_user()
