from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('another/', views.another_page, name='another_page'),
    path('projects/', views.ProjectsListView.as_view(), name='projects_list'),
    path('projects/<int:project_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.TaskDetaiView.as_view(), name='task_detail'),
    path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('projects/create/', views.CreatProjectView.as_view(), name='project_create'),
    path('projects/<int:project_id>/add_task/', views.AddTaskView.as_view(), name='add_task'),
    path('projects/<int:project_id>/update/', views.ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:project_id>/tasks/<int:task_id>/update/', views.TaskUpdateView.as_view(), name='task_update'),
    path('projects/<int:project_id>/delete/', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:project_id>/tasks/<int:task_id>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]