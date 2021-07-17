from django.db import models

# Create your models here.
class Customer(models.Model):
    cust_name       = models.CharField(max_length=50,null=False,primary_key=True)
    cust_id         = models.PositiveIntegerField(unique=True)
    cust_address    = models.CharField(max_length=70,null=False)

    def __str__(self):
        return self.cust_name

class Revenue(models.Model):
    cust_id                = models.ForeignKey('Customer',null=False,on_delete=models.PROTECT)
    invoice_amount_euro     = models.DecimalField(decimal_places=2,null=False,max_digits=6)
    transaction_date        = models.DateField(null=False)
    revenue_charged_euro    = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    cost_of_goods_euro      = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    account_invoice_received = models.PositiveIntegerField(null=False)
    revenue_account_name  = models.CharField(max_length=50,null=False,default=111001)
    operational_costs_euro  = models.DecimalField(default=0,decimal_places=2,max_digits=6)

   # @property
   # def _get_revenue_charged_euro(self):
   #         #Returns 10% of amount received as revenue (rest 90% is either services or goods delievered to the customer)
   #         return  self.invoice_amount_euro * 0.1
   # revenue_charged_euro = property(_get_revenue_charged_euro)

    def __str__(self):
        return self.revenue_account_name
        return self.cust_id              #not returning chk with foreign key ask


#class GM(models.Model):
 #   revenue_account_rollup  = models.DecimalField(decimal_places=2,null=False,max_digits=6)
  #  invoice_account_rollup  = models.DecimalField(decimal_places=2,null=False,max_digits=6)
   # cogs_rollup             = models.DecimalField(decimal_places=2,null=False,max_digits=6)
    # Margin_takeout_amt      = models.DecimalField(decimal_places=2,null=False,max_digits=6)


