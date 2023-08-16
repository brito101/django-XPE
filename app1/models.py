from django.db import models


class User(models.Model):
    name = models.CharField("name", max_length=30)
    phone = models.BigIntegerField("phone")
    email = models.EmailField("email", max_length=30)

    def __str__(self):
        return f"Nome: {self.name}, telefone: {self.phone}, email: {self.email}"
