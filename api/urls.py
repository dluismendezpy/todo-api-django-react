# Django
from django.urls import path

# Own
from . import views


urlpatterns = [
    path("", views.api_overview, name="api_overview"),
    path("task-list/", views.task_list, name="task_list"),
    path("task-create/", views.task_create, name="task_create"),
    path("task-detail/<str:pk>/", views.task_detail, name="task_detail"),
    path("task-update/<str:pk>/", views.task_update, name="task_update"),
    path("task-delete/<str:pk>/", views.task_delete, name="task_delete")
]
