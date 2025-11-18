from ninja import ModelSchema, Schema
from typing import Optional
from .models import *
from datetime import date
from uuid import UUID

class OrderIn(ModelSchema):
    class Config:
        model = Order
        model_exclude = ["id", "jobcard"]

class OrderOut(ModelSchema):
    class Config:
        model = Order
        model_fields = "__all__"

class JobcardIn(ModelSchema):
    
    cust_id: Optional[UUID] = None
    unreg_customer: Optional[str] = None
    unreg_contact: Optional[str] = None
    orders : list[OrderIn]
    
    class Config:
        model = Jobcard
        model_exclude = ["id"]

class JobcardOut(ModelSchema):
    class Config:
        model = Jobcard
        model_fields = "__all__"

class EstimateOut(ModelSchema):

    class Config:
        model=Jobcard
        model_fields = "__all__"
        model_exclude = ["id"]
    orders : list[OrderOut] = []

class ContactSchema(ModelSchema):
    class Config:
        model = Contact
        model_exclude = ["id"]
        model_fields_optional = "__all__"

class ContactPatchSchema(Schema):
    acc_type : Optional[str] = None
    type_of_contact : Optional[str] = None
    company_name : Optional[str] = None
    name : Optional[str] = None
    display_name : Optional[str] = None
    contact : Optional[str] = None
    alt_contact : Optional[str] = None
    email : Optional[str] = None
    taxable : Optional[bool] = None
    gstin : Optional[str] = None
    opening_balance : Optional[float] = None
    closing_balance : Optional[float] = None

class CustomerIN(ModelSchema):
    class Config:
        model = Contact
        model_exclude = ["id", "closing_balance"]
        model_fields_optional = "__all__"

class ItemSchema(ModelSchema):
    class Config:
        model = Item
        model_exclude = ["id"]
        model_fields_optional = "__all__"

class ItemPatchSchema(Schema):
    type : Optional[str] = None
    code : Optional[str] = None
    item : Optional[str] = None
    unit : Optional[str] = None
    hsn_code : Optional[str] = None
    tax_preference : Optional[str] = None
    taxrates : Optional[float] = None
    purchase_rate : Optional[float] = None
    sales_rate : Optional[float] = None


