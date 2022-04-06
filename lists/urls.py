from django.urls import path
from  . import views

urlpatterns=[
    path('',views.todas_tarefas,name='todas_tarefas'),
    path('delete/<id>/',views.deletar_tarefa,name='delete'),
    path('editar/<id>/',views.editar_tarefa,name='editar'),
]