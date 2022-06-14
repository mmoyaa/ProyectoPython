from importlib.resources import path
from readline import append_history_file
from django import views
from views import bloglistview


app_name = 'blog';
urlpatterns = [
   path('', bloglistview.as_view(), name='blog_list'),
];
