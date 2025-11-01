from django.db import models

# Create your models here.
class Products(models.Model):

    CATEGORY_CHOICES = [
        ('Limpieza', 'Limpieza'),
        ('Bebidas', 'Bebidas'),
        ('Abarrote', 'Abarrote'),
        ('Sabritas', 'Sabritas'),
        ('Galletas', 'Galletas'),
        ('Dulces', 'Dulces'),
        ('Papeleria', 'Papeleria'),
        ('Vitrina', 'Vitrina'),
        ('Cuidado Personal', 'Cuidado_personal'),
        ('Lacteos', 'Lacteos'),
    ]

    name = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='abarrote', verbose_name="Categoría")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    barcode = models.CharField(max_length=50, unique=True, verbose_name='Código de barra', blank=True)

    def __str__(self):
        return self.name


