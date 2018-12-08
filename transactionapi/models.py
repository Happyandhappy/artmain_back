from django.db import models
from mongoengine import Document, fields

# Create your models here.

class F0000Z1(Document):
    tanant = fields.StringField()
    tablename = fields.StringField()
    fieldname = fields.StringField()
    reportingname = fields.StringField()
    groupcode = fields.StringField()
    groupdescription = fields.StringField()
