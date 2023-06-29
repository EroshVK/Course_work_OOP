from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """
    Абстрактный класс для работы с API
    """
    @abstractmethod
    def get_vacancies(self, keyword, pages):
        pass

    @abstractmethod
    def process_vacancies(self, data):
        pass
