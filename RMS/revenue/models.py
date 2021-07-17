from django.db import models

# Create your models here.
class Customers(models.Model):
    customer_name   = models.CharField(max_length=50,null=False)
    cust_id         = models.PositiveIntegerField(unique=True)
    cust_address    = models.CharField(max_length=70,null=False)

    def __str__(self):
        return self.customer_name
        return self.cust_address

class Revenue(models.Model):
    cust_name                = models.CharField(max_length=50,null=False)
    cust_id                 = models.PositiveIntegerField(unique=True)
    invoice_amount_euro     = models.DecimalField(decimal_places=2,null=False,max_digits=6)
    transaction_date        = models.DateField(null=False)
    revenue_charged_euro    = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    cost_of_goods_euro      = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    account_invoice_received = models.PositiveIntegerField(null=False)
    revenue_account_number  = models.PositiveIntegerField(null=False)
    operational_costs_euro  = models.DecimalField(default=0,decimal_places=2,max_digits=6)

    def __str__(self):
        return self.revenue_account_number

#class GM(models.Model):
 #   revenue_account_rollup  = models.DecimalField(decimal_places=2,null=False,max_digits=6)
  #  invoice_account_rollup  = models.DecimalField(decimal_places=2,null=False,max_digits=6)
   # cogs_rollup             = models.DecimalField(decimal_places=2,null=False,max_digits=6)
    # Margin_takeout_amt      = models.DecimalField(decimal_places=2,null=False,max_digits=6)


