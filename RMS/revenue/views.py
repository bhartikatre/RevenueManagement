from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from revenue.models import Revenue,Customer
#from django.views import Revenue
#from .models import   -- ??

# Create your views here.
class RevenueList(ListView):
    model = Revenue
    template_name = 'listrev.html'
    context_object_name = 'revenuecontext'

class Details(DetailView):
    model = Revenue
    template_name = 'detail_rev.html'
    context_object_name = 'detailcontext'

#class CreateRev(CreateView):
 #   model = Revenue
 #   template_name = 'create_rev.html'
 #   context_object_name = 'createcontext'

class UpdateRev(UpdateView):
    model = Revenue
    template_name = 'update_rev.html'
    context_object_name = 'updatecontext'

    #def get(self,request):
    #return HttpResponse(f"Hello this is the page")
    #listrev = Revenue.objects.all()
    #context = {'listrev': listrev}
    #total_revenue = .count or other method for rev sum
       # return render(request, 'listrev.html')             #, context=context)