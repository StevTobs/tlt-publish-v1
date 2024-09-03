from django.contrib import admin
from tltapp.models import Datacustomer
# Register your models here.


class StatementAdmin(admin.ModelAdmin):
    list_display =[
        "picplace",
      
    ]
admin.site.register(Datacustomer,StatementAdmin)