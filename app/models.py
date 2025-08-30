from django.db import models
import uuid

# Create your models here.
class Jobcard(models.Model):

    jobno = models.CharField(max_length=10, unique=True)
    job_date = models.DateField(auto_created=True, auto_now_add=True)
    # order_id = models.IntegerField()
    cust_id = models.IntegerField()
    taxable_amount = models.FloatField(null=True, blank=True)
    tax_amount = models.FloatField(null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)
    grandtotal = models.FloatField()
    advance = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.jobno}-{self.job_date}'

class Order(models.Model):
    # jobno = models.CharField(max_length=5)
    jobcard = models.ForeignKey(Jobcard, on_delete=models.CASCADE, related_name="orders")
    account = models.CharField(max_length=100) # Sales or Purchase
    item_no = models.SmallIntegerField()
    item = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    qty = models.FloatField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    tax_rate = models.FloatField(null=True, blank=True)
    tax_amount = models.FloatField(null=True, blank=True)
    amount = models.FloatField()

class Contact(models.Model):
    cust_id = models.UUIDField(default=uuid.uuid4, editable=False)
    acc_type = models.CharField(max_length=10) # Sales or Purchase
    type_of_contact = models.CharField(max_length=10) # Customer or Vendor
    company_name = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    display_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    alt_contact = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    taxable = models.BooleanField(default=False, null=True, blank=True)
    gstin = models.CharField(max_length=20, null=True, blank=True)
    opening_balance = models.FloatField(default=0.0)
    closing_balance = models.FloatField(default=0.0)

class TaxRates(models.Model):
    slab = models.CharField(max_length=10, unique=True)
    rate = models.DecimalField(max_digits=3, decimal_places=2, unique=True)


class Item(models.Model):
    code = models.CharField(max_length=20, null=True, blank=True)
    item = models.CharField(max_length=50, null=True, blank=True)
    hsn_code = models.CharField(max_length=20, null=True, blank=True)
    taxrates = models.ForeignKey(TaxRates, on_delete=models.CASCADE, related_name="taxes")
    purchase_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sales_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    