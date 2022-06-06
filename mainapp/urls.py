from rest_framework.routers import SimpleRouter
from django.urls import path
from mainapp.views import(
    AboutMeRead, ProjectsCategoryRead, 
    ProjectRead, ContactRead,SendMailView
)

router = SimpleRouter()
router.register('about_me', AboutMeRead)
router.register('categories', ProjectsCategoryRead)
router.register('projects', ProjectRead)
router.register('contacts', ContactRead)

urlpatterns = [
    path('send_mail/', SendMailView.as_view()),
]

urlpatterns += router.urls
