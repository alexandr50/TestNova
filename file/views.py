
from rest_framework import generics
from rest_framework.response import Response

from .models import File
from .serializers import FileCreateSerializer
from .services import Fileloader, GoogleApi
from .services import PATH_TO_TEST_FILE


class FileCreateView(generics.CreateAPIView):
    """Вью для создание файла в google drive"""
    serializer_class = FileCreateSerializer
    queryset = File.objects.all()

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = self.request.POST.get('name')
            data = self.request.POST.get('data')  # получаем данные из request
            file = Fileloader(PATH_TO_TEST_FILE, data)  # создаем обьект класса Fileloader
            file.create_file()  # записываем в файл полученные данные
            google_obj = GoogleApi(PATH_TO_TEST_FILE)  # создаем обьект класса GoogleApi
            google_obj.get_folder_id()  # находим папку в google_drive в  которую будем сохранять
            google_obj.create_file_in_google_drive(name)  # создаем файл в google_drive
            file.delete_file()  # удаляем тестовый файл
            return Response('Файл создан')
