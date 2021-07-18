from django.urls import path
from .views import home_page, student_list, student_add, student_detail, student_update, student_delete, HomeView, StudentList, StudentAdd, StudentDetail, StudentUpdate, StudentDelete
from django.views.generic import TemplateView

urlpatterns = [
    # path('', home_page, name="home"),
    path('', TemplateView.as_view(template_name="fscohort/home.html"), name="home"),
    path('', HomeView.as_view(), name="home"),
    # path('list/', student_list, name="list"),
    path('list/', StudentList.as_view(), name="list"),
    # path('add/', student_add, name="add"),
    path('add/', StudentAdd.as_view(), name="add"),
    # path('<int:id>', student_detail, name="detail"),
    path('<int:id>', StudentDetail.as_view(), name="detail"),
    # path('<int:id>/update', student_update, name="update"),
    path('<int:pk>/update', StudentUpdate.as_view(), name="update"),
    # path('<int:id>/delete', student_delete, name="delete"),
    path('<int:pk>/delete', StudentDelete.as_view(), name="delete"),
]
