import requests
import os

from classes.abstract_api import AbstractAPI
from classes.vacancies_cls import Vacancies


class SuperJobAPI(AbstractAPI):
    """
    Класс для работы с API HeadHunter
    """
    sj_api_key = os.environ.get('SJ_API')

    def __init__(self):
        self.url = 'https://api.superjob.ru/2.0/'
        self.header = {'X-Api-App-Id': self.sj_api_key}

    def get_vacancies(self, keyword, pages):
        """
        Метод для получения вакансий по ключевому слову
        """
        endpoint = 'vacancies/?keyword='
        url = f'{self.url}{endpoint}{keyword}'
        params = {'keyword': keyword,
                  'page': 0,
                  'count': 100}
        response = []
        for page in range(pages):
            params.update({'page': page})
            data = requests.get(url, params=params, headers=self.header)
            response += data.json()['objects']
        return response

    def process_vacancies(self, data):
        """
        Метод для обработки вакансий
        """
        vacancies = [
            Vacancies(title=item['profession'],
                      salary=item['payment_from'],
                      experience=item['experience']['title'],
                      description=item['client'].get('description'),
                      area=item['town']['title'],
                      link=item['link'])
            for item in data]
        return vacancies
