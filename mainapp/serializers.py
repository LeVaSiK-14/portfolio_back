from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from mainapp.tasks import send_mail_to_email

from mainapp.models import(
    AboutMe, ProjectsCategory, Project,
    ProjectsImage, Contact, SendMail
)


class AboutMeSerializers(ModelSerializer):
    class Meta:
        model = AboutMe
        fields = (
            'full_name', 'description', 'photo',
        )


class ProjectsCategorySerializer(ModelSerializer):
    class Meta:
        model = ProjectsCategory
        fields = (
            'title', 'pre_description', 'description', 'image',
        )


class ProjectsImageSerializer(ModelSerializer):
    class Meta:
        model = ProjectsImage
        fields = (
            'project', 'image',
        )


class ProjectSerializer(ModelSerializer):
    images = ProjectsImageSerializer(many=True)
    category_name = serializers.ReadOnlyField(source='category.title')
    class Meta:
        model = Project
        fields = (
            'category_name',
            'name', 'pre_description', 'description',
            'image', 'link', 'date_develop', 'images',
            
        )


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'logo', 'link', 'name',
        )
        
        
class ProjectsCategorySerializer(ModelSerializer):
    projects = ProjectSerializer(many=True)
    class Meta:
        model = ProjectsCategory
        fields = (
            'title', 'pre_description', 'description', 
            'image', 'projects',
        )
        
class SendMailSerializer(ModelSerializer):
    class Meta:
        model = SendMail
        fields = ('full_name', 'email', 'message', 'phone_number', 'date')
        read_only_fields = ('date',)
        
    def create(self, validated_data):
        send_mail_to_email.delay(
            validated_data['full_name'],
            validated_data['email'],
            validated_data['message'],
            validated_data['phone_number'])
        return super().create(validated_data)
