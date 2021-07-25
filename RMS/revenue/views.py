from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from revenue.models import Revenue,Customer
#from django.views import Revenue
#from .models import   -- ??

# Create your views here.
class RevenueList(ListView):
    model = Revenue
    template_name = 'listrev.html'
    context_object_name = 'revenuecontext'
    #def get(self,request):
    #return HttpResponse(f"Hello this is the page")
    #listrev = Revenue.objects.all()
    #context = {'listrev': listrev}
    #total_revenue = .count or other method for rev sum
       # return render(request, 'listrev.html')             #, context=context)