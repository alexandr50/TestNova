
from rest_framework import generics
from rest_framework.response import Response

from .models import File
from .serializers import FileCreateSerializer
from .services import Fileloader, GoogleApi
from .services import path


class FileCreateView(generics.CreateAPIView):
    serializer_class = FileCreateSerializer
    queryset = File.objects.all()

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = self.request.POST.get('name')
            data = self.request.POST.get('data')
            file = Fileloader(path, data)
            file.create_file()
            google_obj = GoogleApi(path)
            google_obj.get_folder_id()
            google_obj.create_file_in_google_drive(name)
            file.delete_file()
            return Response('Файл создан')
