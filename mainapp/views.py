from rest_framework.viewsets import ReadOnlyModelViewSet

from mainapp.serializers import(
    AboutMeSerializers, ProjectsCategorySerializer,
    ContactSerializer, ProjectSerializer,SendMailSerializer
)
from mainapp.models import(
    AboutMe, ProjectsCategory, 
    Project, Contact,SendMail
)
from rest_framework.generics import CreateAPIView


class AboutMeRead(ReadOnlyModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializers
    
    
class ProjectsCategoryRead(ReadOnlyModelViewSet):
    queryset = ProjectsCategory.objects.all()
    serializer_class = ProjectsCategorySerializer
    
    
class ProjectRead(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    
class ContactRead(ReadOnlyModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class SendMailView(CreateAPIView):
    queryset = SendMail.objects.all()
    serializer_class = SendMailSerializer
