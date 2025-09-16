from home import views
from django.urls import path

urlpatterns = [
    path("",views.home),
    path("about/",views.about),
    path("prediction/",views.prediction),
    path("contact/",views.contact),
    path("login/",views.login),
    path("registration/",views.registration),
    
]
