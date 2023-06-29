import json
import os
from abc import abstractmethod, ABC
from typing import List

from classes.vacancies_cls import Vacancies


class Handler(ABC):
    """
    Абстрактный класс для добавления, получения и удаления данных о вакансиях
    """
    @abstractmethod
    def add_vacancy(self, vacancies: Vacancies):
        pass

    @abstractmethod
    def get_vacancy(self, keyword: str):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancies: Vacancies):
        pass


class JSONHandler(Handler):
    """
    Класс для добавления, получения и удаления данных о вакансиях в json файле
    """
    def __init__(self, filename):
        self.__filename = filename
        if not os.path.isfile(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    @property
    def file(self):
        return self.__filename

    @file.setter
    def file(self, name):
        self.__filename = name

    def add_vacancy(self, vacancies: Vacancies):
        """
        Метод для добавления вакансий в json файл
        """
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
        except FileNotFoundError:
            file_data = []
        file_data.append(vacancies.__dict__)  # Преобразование вакансии в словарь
        with open(self.__filename, 'w', encoding='utf') as f:
            json.dump(file_data, f, indent=4, ensure_ascii=False)

    def get_vacancy(self, keyword: str):
        """
        Метод для получения вакансий из json файла
        """
        found_vacancies = []
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                file_data = json.load(f)
        except FileNotFoundError:
            return []
        for item in file_data:
            if keyword.lower() in item['title'].lower():
                found_vacancies.append(item)
        return found_vacancies

    def remove_vacancy(self, vacancies: Vacancies):
        """
        Метод для удаления вакансий из json файла
        """
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                file_name = json.load(f)
        except FileNotFoundError:
            return
        updated_data = [item for item in file_name if item['name'].lower() != vacancies.title.lower()]
        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(updated_data, f, indent=4, ensure_ascii=False)
