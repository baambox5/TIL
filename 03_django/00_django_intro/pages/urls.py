from django.urls import path
from . import views

urlpatterns = [
    # 원래 app url은 아래로 작성해나간다.
    path('index/', views.index),
    path('introduce/', views.introduce),
    path('dinner/', views.dinner),
    path('image/', views.image),
    path('hello/<name>/', views.hello),
    path('intro/<name>&<age>/', views.intro),
    path('multi/<int:num_1>&<int:num_2>/', views.multi),
    path('round-width/<int:radius>/', views.round_width),
    path('template_language/', views.template_language),
    path('gwangbok/', views.isitgwangbok),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('art/', views.art),
    path('result/', views.result),
    path('user_new/', views.user_new),
    path('user_create/', views.user_create),
    path('static_example/', views.static_example),
]