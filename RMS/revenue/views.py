from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from revenue.models import Revenue,Customer
from django.urls import reverse_lazy
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

class CreateRev(CreateView):
    model = Revenue
    template_name = 'create_rev.html'
    success_url = reverse_lazy('revenue')
    fields = '__all__'

class UpdateRev(UpdateView):
    model = Revenue
    template_name = 'update_rev.html'
    context_object_name = 'updatecontext'
    success_url = reverse_lazy('revenue')
    fields = '__all__'
    #def get(self,request):
    #return HttpResponse(f"Hello this is the page")
    #listrev = Revenue.objects.all()
    #context = {'listrev': listrev}
    #total_revenue = .count or other method for rev sum
       # return render(request, 'listrev.html')             #, context=context)
class PnL(ListView):
    model = Revenue
    template_name = 'pnl.html'
    context_object_name =  'pnlcontext'
    # for a date range
    #def Calpnl(self,*args,**kwargs):
    #    for i in pnlcontext:
    #        profit_loss = i.revenue_charged_euro - (i.cost_of_goods_euro + i.cost_of_goods_euro)
    #    if profit_loss > 0
    #            "its profit" image green arrow with toal amount
    #    else
    #            "its loss" image red with toal amt



