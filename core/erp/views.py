from multiprocessing import context
from django.shortcuts import render
from django.views import generic

from.models import Category

# Create your views here.
def category_list(request):
    data = {
        'title':'Listado de Categorías',
        'categories':Category.objects.all()
    }
    return render(request, 'erp/list.html',data)


class CategoryListView(generic.ListView):

    model = Category
    template_name = 'erp/list.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
