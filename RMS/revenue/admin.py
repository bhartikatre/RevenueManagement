from django.contrib import admin
from .models import Revenue,Customer

# Register your models here
#admin.site.register(Revenue,RevenueAdmin)
admin.site.register(Revenue)
admin.site.register(Customer)

#class RevenueAdmin(admin.ModelAdmin):
 #   list_display = ['cust_name','cust_id','invoice_amount_euro','transaction_date','cost_of_goods_euro','account_invoice_received',
 #                  'revenue_account_name','operational_costs_euro','revenue_charged_euro']
    #readonly_fields = ('revenue_charged_euro')