from django.db import models


class AboutMe(models.Model):
    full_name = models.CharField(max_length=127, verbose_name='ФИО')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to='my_photo/', verbose_name='Фото')

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

    def __str__(self):
        return self.full_name


class ProjectsCategory(models.Model):
    title = models.CharField(max_length=127, verbose_name='Название категории')
    pre_description = models.CharField(max_length=127, verbose_name='Первоночальное описание')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Картинка', upload_to='project_categories/')

    class Meta:
        verbose_name = 'Категория проектов'
        verbose_name_plural = 'Категории проектов'

    def __str__(self):
        return self.title


class Project(models.Model):
    category = models.ForeignKey(ProjectsCategory, on_delete=models.CASCADE, verbose_name='Категория', related_name='projects')
    name = models.CharField(max_length=127, verbose_name='Название')
    pre_description = models.CharField(max_length=127, verbose_name='Первоночальное описание')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Картинка', upload_to='projects/')
    link = models.URLField(max_length=511, verbose_name='Ссылка на проект')
    date_develop = models.CharField(max_length=127, verbose_name='Время разработки')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class ProjectsImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект', related_name='images')
    image = models.ImageField(verbose_name='Картинка', upload_to='projects/carusel')

    class Meta:
        verbose_name = 'Картинки проекта'
        verbose_name_plural = 'Картинки проектов'
        
    def __str__(self):
        return self.project.name


class Contact(models.Model):
    logo = models.ImageField(upload_to='contacts_logo/', verbose_name='Лого соц. сети')
    link = models.URLField(max_length=511, verbose_name='Ссылка на соц. сеть')
    name = models.CharField(max_length=127, verbose_name='Название соц. сети')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        self.name
        
class SendMail(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.email} -- {self.date}'
