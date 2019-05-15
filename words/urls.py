from django.urls import path , include
from . import views

urlpatterns = [
    path('add',views.add,name='add'),
    path('<int:word_id>',views.detail,name='detail'),
    path('<int:word_id>/important',views.important,name='important'),
    path('result',views.result,name='result'),

]