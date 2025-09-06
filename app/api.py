from ninja import NinjaAPI
from ninja.responses import Response
from typing import List
from django.shortcuts import get_object_or_404
from .models import *
from .schemas import *
from django.db.models import Q, Max
# from urllib.parse import unquote
from uuid import UUID

api = NinjaAPI()

@api.get("/nextjobno")
def nextjobno(request):
    last_jobcard = Jobcard.objects.aggregate(Max("jobno"))["jobno__max"] or "0"
    return str(int(last_jobcard)+1).zfill(5)


@api.post("/estimate/create", response=JobcardOut)
def create_estimate(request, payload:JobcardIn):
    jobcard = Jobcard.objects.create(**payload.dict(exclude={"orders"}))

    for order in payload.orders:
        Order.objects.create(jobcard=jobcard, **order.dict())

    return jobcard

@api.get("/jobcard", response=list[JobcardOut])
def all_jobcard(request):
    jobcard = Jobcard.objects.prefetch_related("orders").all().order_by("-jobno")
    return jobcard

@api.get("/estimate/{slug}", response=EstimateOut)
def get_jobcard(request, slug:str):
    jobcard = Jobcard.objects.prefetch_related("orders").get(jobslug=slug)
    return {
        "jobslug" : jobcard.jobslug,
        "jobno": jobcard.jobno,
        "job_date": jobcard.job_date,
        "cust_id": jobcard.cust_id,
        "taxable_amount": jobcard.taxable_amount,
        "tax_amount": jobcard.tax_amount,
        "discount": jobcard.discount,
        "grandtotal": jobcard.grandtotal,
        "orders": list(jobcard.orders.all())
    }



#CONTACT REQUEST METHODS ( FOR CUSTOMER AND VENDOR BOTH CRUD)
@api.post("/contact/create", response=CustomerIN)
def create_contact(request, payload:CustomerIN):
    contact = Contact.objects.create(**payload.dict())
    return contact

@api.get("/contact", response=list[ContactSchema])
def all_contact(request):
    contact = Contact.objects.all()
    return contact

@api.get("/contact/{slug}", response=list[ContactSchema])
def get_contact(request, slug:str):
    try:
        contact = Contact.objects.filter(Q(display_name__icontains=slug)|Q(name__icontains=slug)|Q(company_name__icontains=slug)|Q(contact=slug)|Q(gstin=slug)|Q(cust_id=UUID(slug)))
    except ValueError:
        contact = Contact.objects.filter(Q(display_name__icontains=slug)|Q(name__icontains=slug)|Q(company_name__icontains=slug)|Q(contact=slug)|Q(gstin=slug))
    return contact

@api.delete("contact/delete/{slug}", response={200:dict})
def delete_contact(request, slug:str):
    contact = get_object_or_404(Contact, cust_id=UUID(slug))
    contact.delete()
    return {"status":"Deleted"}

@api.patch("/contact/update/{slug}", response=ContactSchema)
def update_contact(request, slug:str, payload:ContactPatchSchema):
    contact = get_object_or_404(Contact, cust_id=UUID(slug))
    update_data = payload.dict(exclude_unset=True)

    for attr, value in update_data.items():
        setattr(contact, attr, value)
    contact.save()
    return contact

@api.get("/customer/all", response=list[ContactSchema])
def all_customers(request):
    customers = Contact.objects.filter(Q(type_of_contact="customer")|Q(acc_type="sales"))
    return customers

@api.get("/vendor/all", response=list[ContactSchema])
def all_vendors(request):
    vendors = Contact.objects.filter(Q(type_of_contact="vendor")|Q(acc_type="purchase"))
    return vendors


# PRODUCT (ITEMS) REQUEST METHODS
@api.post("/item/create", response=ItemSchema)
def create_item(request, payload:ItemSchema):
    item = Item.objects.create(**payload.dict(exclude_unset=True))
    return item

@api.get("item/all", response=list[ItemSchema])
def get_items(request):
    items = Item.objects.all().order_by("item")
    return items

@api.get("item/{slug}", response=list[ItemSchema])
def get_item(request, slug:str):
    try:
        item = Item.objects.filter(Q(type__icontains=slug)|Q(item__icontains=slug)|Q(code__icontains=slug)|Q(item_id=UUID(slug)))
    except ValueError:
        item = Item.objects.filter(Q(type__icontains=slug)|Q(item__icontains=slug)|Q(code__icontains=slug))
    return item

@api.patch("item/update/{slug}", response=ItemSchema)
def update_item(request, slug:str, payload:ItemPatchSchema):
    item = get_object_or_404(Item, item_id=UUID(slug))
    update_data = payload.dict(exclude_unset=True)

    for attr, value in update_data.items():
        setattr(item, attr, value)
    item.save()
    return item

@api.delete("item/delete/{slug}", response={200:dict})
def delete_item(request, slug:str):
    item = get_object_or_404(Item, item_id=UUID(slug))
    item.delete()
    return {"status" : "Deleted"}
