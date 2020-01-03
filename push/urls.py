from django.conf.urls import url
from django.urls import path


from push import views

urlpatterns = [
    path('', views.device_list),
]