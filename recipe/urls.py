from django.urls import path

from recipe.views import home,about,contact


urlpatterns = [
    path('', home),
    path('about/', about),
    path('contact/', contact),

]
