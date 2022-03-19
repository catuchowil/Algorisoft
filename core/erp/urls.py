from django.urls import path

from .views import category_list, CategoryListView

urlpatterns = [
    #path('category/list/',category_list, name='category_list'),

    path('category/list/',CategoryListView.as_view(), name='category_list'),
]