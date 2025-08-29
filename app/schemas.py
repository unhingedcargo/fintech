from ninja import ModelSchema, Schema
from typing import Optional
from .models import *
from datetime import date

class OrderIn(ModelSchema):
    class Config:
        model = Order
        model_exclude = ["id", "jobcard"]

class OrderOut(ModelSchema):
    class Config:
        model = Order
        model_fields = "__all__"

class JobcardIn(ModelSchema):
    orders : list[OrderIn]

    class Config:
        model = Jobcard
        model_exclude = ["id", "job_date"]

class EstimateOut(ModelSchema):

    class Config:
        model=Jobcard
        model_fields = "__all__"
        model_exclude = ["id"]
    orders : list[OrderOut] = []

class JobcardOut(ModelSchema):
    class Config:
        model = Jobcard
        model_fields = "__all__"

class ContactSchema(ModelSchema):
    class Config:
        model = Contact
        model_exclude = ["id"]
        model_fields_optional = "__all__"

class ContactPatchSchema(Schema):
    display_name: Optional[str] = None
    name: Optional[str] = None
    company_name: Optional[str] = None
    contact: Optional[str] = None
    alt_contact: Optional[str] = None
    email: Optional[str] = None
    gstin: Optional[str] = None
    acc_type: Optional[str] = None
    type_of_contact: Optional[str] = None
    opening_balance: Optional[float] = None
    closing_balance: Optional[float] = None
    taxable: Optional[bool] = None

class CustomerIN(ModelSchema):
    class Config:
        model = Contact
        model_exclude = ["id", "closing_balance"]

class ItemSchema(ModelSchema):
    class Config:
        model = Item
        model_exclude = ["id"]
