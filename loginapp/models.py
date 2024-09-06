from django.db import models

# Create your models here.
class User(models.Model):
    username   = models.CharField(max_length=100)
    password   = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    tel        = models.CharField(max_length=100)
    province   = models.CharField(max_length=100)
    business   = models.CharField(max_length=100)
    email     =  models.CharField(max_length=100)

    date       = models.DateField(auto_now_add=True)

    # # convert object to string
    def __str__(self):
        return " ชื่อ : " + self.first_name + ' ' +self.last_name +', จังหวัด : ' + str(self.province)