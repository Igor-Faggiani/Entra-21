import os
from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_perishable = models.BooleanField()
    explation_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="products", blank=True, null=True)
    enabled = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)
        
    def __delete_file_if_exists(self, file):
        if file and os.path.isfile(file.path):
            os.remove(file.path)
            
    def delete(self, *args, **kwargs):
        self.__delete_file_if_exists(self.photo)
        super(Product, self).delete(*args, **kwargs)
    
class Meta:
    verbose_name = "Produto"
    verbose_name_plural = "Produtos"
    