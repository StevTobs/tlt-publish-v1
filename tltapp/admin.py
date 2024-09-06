from django.contrib import admin
from tltapp.models import Datacustomer
# Register your models here.
from loginapp.models import User

class StatementAdmin(admin.ModelAdmin):
    list_display =[
        "picplace",
      
    ]
admin.site.register(Datacustomer,StatementAdmin)
admin.site.register(User)