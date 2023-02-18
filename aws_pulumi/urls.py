from django.contrib import admin
from django.urls import path

from employee_resources.views import CreatEC2ResourceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ec2-create/', CreatEC2ResourceView.as_view())

]
