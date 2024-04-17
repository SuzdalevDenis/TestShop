from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    genres = models.CharField(max_length=150)

    def __str__(self):
        return self.genres


class BookModel(models.Model):
    title = models.CharField(max_length=128)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE, db_index=True)
    genre = models.ManyToManyField(to='Genre', related_name='books')
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.title

