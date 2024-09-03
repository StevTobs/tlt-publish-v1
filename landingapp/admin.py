from django.contrib import admin
from landingapp.models import Customer
# Register your models here.


class StatementAdmin(admin.ModelAdmin):
    list_display =[
        "name",
        "email",
        "number",
        "message"
    ]
admin.site.register(Customer,StatementAdmin)