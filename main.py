import os.path

from classes.hh_cls import HeadHunterAPI
from classes.data_to_json import JSONHandler
from classes.sj_cls import SuperJobAPI


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
            keyword = input("Введите ключевое слово для запроса: ")
            n = int(input("Введите количество вакансий: "))

            hh = HeadHunterAPI()
            data_hh = hh.get_vacancies(keyword, n)
            processed_vacancies_hh = hh.process_vacancies(data_hh)

            print("Вакансии HeadHunter: ")
            for item in processed_vacancies_hh:
                print(item)

            file_hh = 'vacancies_hh.json'
            if os.path.isfile(file_hh):
                os.remove(file_hh)
            add_hh = JSONHandler(file_hh)
            for item in processed_vacancies_hh:
                add_hh.add_vacancy(item)

        elif choice == "2":
            keyword = input("Введите ключевое слово для запроса: ")
            n = int(input("Введите количество вакансий: "))

            sj = SuperJobAPI()
            data_sj = sj.get_vacancies(keyword, n)
            processed_vacancies_sj = sj.process_vacancies(data_sj)

            print("Вакансии SuperJob: ")
            for item in processed_vacancies_sj:
                print(item)

            file_sj = 'vacancies_sj.json'
            if os.path.isfile(file_sj):
                os.remove(file_sj)
            add_sj = JSONHandler(file_sj)
            for item in processed_vacancies_sj:
                add_sj.add_vacancy(item)

        elif choice == "3":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    interact_with_user()
