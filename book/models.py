from djongo import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'book_categories'

    def __str__(self):
        return self.name


class Book(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    quantity = models.IntegerField(default=1)
    categories = models.ArrayReferenceField(to=Category, on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.name
