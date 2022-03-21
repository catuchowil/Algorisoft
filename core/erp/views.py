from multiprocessing import context
from django.shortcuts import render, redirect

from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.views import generic

from.models import Category
from django.http import JsonResponse

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

    #--Sobreescribo el método dispatch
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args, **kwargs):
        return super().dispatch(request,*args, **kwargs)
    

    def post(self,request,*args, **kwargs):
        data = {}
        try:
            data = Category.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context
