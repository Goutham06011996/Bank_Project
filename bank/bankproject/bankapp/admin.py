from django.contrib import admin

from . models import Branch
from . models import District
from . models import Account

# Register your models here.
admin.site.register(Account)
admin.site.register(District)
admin.site.register(Branch)
