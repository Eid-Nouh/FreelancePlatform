from django.db import models


class Service(models.Model):

    service_type = models.CharField(max_length=100)

    idea_name = models.CharField(max_length=200)

    expected_price = models.IntegerField()

    full_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=20)

    email = models.EmailField()

    def __str__(self):

        return self.idea_name