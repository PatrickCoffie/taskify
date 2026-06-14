from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('wishlist', 'Wish List'),
        ('birthday', 'Birthday'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title