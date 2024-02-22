from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'book_authors'

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'book_publishers'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'book_categories'

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category, related_name='books')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.name
