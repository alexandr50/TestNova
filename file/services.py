import os

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

path = '/home/alexandr/PycharmProjects/TestNova/app/file/data_files/test.txt'


class Fileloader:
    """Класс для работы с файлом"""
    def __init__(self, path, text):
        self.path = path
        self.text = text

    def create_file(self):
        """Создает файл и запичываетв него данные"""

        with open(self.path, 'w') as file:
            file.write(self.text)
            return path

    def delete_file(self):
        """Удаляет файл"""

        os.remove(self.path)


class GoogleApi:
    """Класс для работы google drive"""

    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = '/home/alexandr/PycharmProjects/TestNova/app/file/data_files/data.json'

    def __init__(self, path):
        """Конструктор обьекта создает объект google api client и путь к файлу"""

        self.credentials = service_account.Credentials.from_service_account_file(
            self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.service = build('drive', 'v3', credentials=self.credentials)
        self.path = path

    def get_folder_id(self):
        """Возвращает объект папки в которую будем сохранять файл"""

        results = self.service.files().list(pageSize=30,
                                            fields="nextPageToken, files(id, name, mimeType)").execute()
        for item in results['files']:
            if item['mimeType'].endswith('folder'):
                return item['id']

    def create_file_in_google_drive(self, name):
        """Создает файл с google drive"""
        folder_id = self.get_folder_id()
        file_metadata = {
            'name': name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(self.path, resumable=True)
        self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()


file = Fileloader(path, 'kjjfdfj')
file.create_file()
g = GoogleApi(path)
n = g.get_folder_id()
m = g.create_file_in_google_drive('kfmc')
file.delete_file()
