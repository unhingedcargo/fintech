from ninja import NinjaAPI
from typing import List
from django.shortcuts import get_object_or_404
from .models import *
from .schemas import *
from django.db.models import Q, Max

api = NinjaAPI()

@api.get("/nextjobno")
def nextjobno(request):
    last_jobcard = Jobcard.objects.aggregate(Max("jobno"))["jobno__max"] or "0"
    return str(int(last_jobcard)+1).zfill(6)


@api.post("/estimate/create", response=JobcardOut)
def create_estimate(request, payload:JobcardIn):
    jobcard = Jobcard.objects.create(**payload.dict(exclude={"orders"}))

    for order in payload.orders:
        Order.objects.create(jobcard=jobcard, **order.dict())

    return jobcard

@api.get("/jobcard", response=list[JobcardOut])
def all_jobcard(request):
    jobcard = Jobcard.objects.prefetch_related("orders").all()
    return jobcard

@api.get("/estimate/{id}", response=EstimateOut)
def get_jobcard(request, id:str):
    jobcard = Jobcard.objects.prefetch_related("orders").get(jobno=id)
    return {
        "id": jobcard.id,
        "jobno": jobcard.jobno,
        "job_date": jobcard.job_date,
        "cust_id": jobcard.cust_id,
        "taxable_amount": jobcard.taxable_amount,
        "tax_amount": jobcard.tax_amount,
        "discount": jobcard.discount,
        "grandtotal": jobcard.grandtotal,
        "orders": list(jobcard.orders.all())
    }

@api.post("/contact/create", response=CustomerIN)
def create_customer(request, payload:CustomerIN):
    contact = Contact.objects.create(**payload.dict())
    return contact

@api.get("/contact", response=list[ContactSchema])
def all_contact(request):
    contact = Contact.objects.all()
    return contact

@api.get("/contact/{slug}", response=list[ContactSchema])
def get_contact(request, slug:str):
    contact = Contact.objects.filter(Q(display_name__icontains=slug)|Q(name__icontains=slug)|Q(company_name__icontains=slug)|Q(contact=slug)|Q(gstin=slug))
    return contact

@api.patch("/contact/update/{slug}", response=ContactSchema)
def update_contact(request, slug:str, payload:ContactSchema):
    contact = get_object_or_404(Contact, Q(display_name__icontains=slug) | Q(name__icontains=slug) | Q(company_name__icontains=slug))
    update_data = payload.dict(exclude_unset=True)

    for attr, value in update_data.items():
        setattr(contact, attr, value)
    
    contact.save()
    return contact

@api.get("/customer/all", response=list[ContactSchema])
def all_customers(request):
    customers = Contact.objects.filter(Q(type_of_contact="customer")|Q(acc_type="sales"))
    return customers

@api.get("/vendors/all", response=list[ContactSchema])
def all_vendors(request):
    vendors = Contact.objects.filter(Q(type_of_contact="vendor")|Q(acc_type="purchase"))
    return vendors












# @api.post("/items", response=Job)
# def create_item(request, data: ItemCreateSchema):
#     item = Item.objects.create(**data.dict())
#     return item

# @api.put("/items/{item_id}", response=Job)
# def update_item(request, item_id: int, data: ItemUpdateSchema):
#     item = get_object_or_404(Item, id=item_id)
#     for attr, value in data.dict(exclude_unset=True).items():
#         setattr(item, attr, value)
#     item.save()
#     return item

# @api.delete("/items/{item_id}")
# def delete_item(request, item_id: int):
#     item = get_object_or_404(Item, id=item_id)
#     item.delete()
#     return {"success": True}
