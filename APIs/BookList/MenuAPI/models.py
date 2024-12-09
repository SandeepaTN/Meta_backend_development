from django.db import models

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title

class Menu(models.Model):
    name=models.CharField(max_length=255)
    about=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.PROTECT)
    inventory=models.SmallIntegerField(default=1)
    