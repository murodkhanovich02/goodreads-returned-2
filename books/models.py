from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from users.models import CustomUser


class Authors(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()

    class Meta:
        verbose_name = 'Authora'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.full_name


class Books(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    isbn = models.IntegerField()
    descriptions = models.TextField()
    cover_picture = models.ImageField(default='default_cower.png')

    class Meta:
        verbose_name = 'Books'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)

    comment = models.TextField()
    stars_given = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Review'

    def __str__(self):
        return f"{self.user} - {self.book}: {self.comment}"