from django.urls import path
from .import views

app_name = 'branches'
urlpatterns = [
    path('next={<str:next>}/', views.SelectBranch.as_view(), name='select-branch'),
]
