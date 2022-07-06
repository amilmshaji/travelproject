from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    # path('',views.operation,name='operation'),
    # path('result/',views.result,name="result"),
]
