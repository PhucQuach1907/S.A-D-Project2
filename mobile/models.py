from djongo import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mobile_type'
        ordering = ['name']


class Mobile(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    type = models.ArrayReferenceField(to=Type, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = 'mobiles'
        ordering = ['name']

    def __str__(self):
        return self.name
