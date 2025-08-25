from ninja import ModelSchema, Schema
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

class CustomerIN(ModelSchema):
    class Config:
        model = Contact
        model_exclude = ["id", "closing_balance"]

class ItemSchema(ModelSchema):
    class Config:
        model = Item
        model_exclude = ["id"]
