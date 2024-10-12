from django.db import models

class Seller(models.Model):
    name = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='materials')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
