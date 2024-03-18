from djongo import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'clothes_type'
        ordering = ['name']

    def __str__(self):
        return self.name


class Clothes(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=50)
    brand_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=18, decimal_places=2)
    type = models.ArrayReferenceField(to=Type, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'clothes'

    def __str__(self):
        return self.name
