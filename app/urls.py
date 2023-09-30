from django.urls import path
from app import views

urlpatterns = [
    
    path('addtask/',views.addtask,name='addtask'),
    path('markdone/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    path('markundo/<int:pk>/',views.mark_as_undo,name='mark_as_undo'),
    path('deletetask/<int:pk>/',views.delete_task,name='delete_task'),
    
]
