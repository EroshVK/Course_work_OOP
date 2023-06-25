import requests

from classes.abstract_api import AbstractAPI
from classes.vacancies_cls import Vacancies


class HeadHunterAPI(AbstractAPI):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self):
        self.url = 'https://api.hh.ru/'
        self.header = {'User-Agent': 'user_agent_hh'}

    def get_vacancies(self, keyword, count):
        """
        Метод для получения вакансий по ключевому слову
        """
        if count > 100:
            pages = int(count / 10) + 1
        else:
            pages = 1
        endpoint = 'vacancies?text='
        url = f'{self.url}{endpoint}{keyword}'
        params = {'keyword': keyword,
                  'page': 0,
                  'per_page': count}
        response = []
        for page in range(pages):
            params.update({'page': page})
            data = requests.get(url, params=params, headers=self.header)
            response += data.json()['items']
        return response

    def process_vacancies(self, data):
        """
        Метод для обработки вакансий
        """
        vacancies = [
            Vacancies(title=item['name'],
                      salary=item['salary']['to'] if item['salary'] else None,
                      experience=item['experience']['name'],
                      description=item['snippet']['responsibility'],
                      area=item['area']['name'],
                      link=item['alternate_url'])
            for item in data]
        return vacancies
