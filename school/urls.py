from django.urls import path
from .views import *

app_name = 'school'
url_string = '<str:grade_name>/<str:chapter_name>/'
urlpatterns = [
    path('', school_view, name='school-view'),
    path('<str:grade_name>/', chapters_list_view, name='chapters-list'),
    path('<str:grade_name>/<str:chapter_name>/', numericals_list_view, name='numericals-list'),
    path('<str:grade_name>/<str:chapter_name>/numerical-create/', numerical_create_view, name='numerical-create'),
    path('<str:grade_name>/<str:chapter_name>/<int:numerical_id>/edit/', numerical_edit_view, name='numerical-edit'),
    path('<str:grade_name>/<str:chapter_name>/<int:numerical_id>/delete/', numerical_delete_view,
         name='numerical-delete')

]
