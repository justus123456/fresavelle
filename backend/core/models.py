from django.db import models
from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, max_length=2000)
    unit = models.CharField(max_length=80, help_text='A fixed selling unit, e.g. 500 g pack or 1 basket.')
    price_kobo = models.PositiveIntegerField(help_text='Price in kobo; 100 kobo = one naira.')
    stock = models.PositiveIntegerField(default=0, help_text='Number of fixed units available. Baskets are counted independently.')
    is_basket = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    image_path = models.CharField(max_length=200, blank=True, validators=[RegexValidator(r'^/images/[a-zA-Z0-9_-]+\.(png|jpg|jpeg|webp)$', 'Use a local image path under /images/.')])
    class Meta:
        ordering = ['id']
        constraints = [models.CheckConstraint(condition=models.Q(price_kobo__gte=0), name='product_price_nonnegative'), models.CheckConstraint(condition=models.Q(stock__gte=0), name='product_stock_nonnegative')]
    def __str__(self):
        return f'{self.name} ({self.unit})'
