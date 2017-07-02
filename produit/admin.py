from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Boutique, Produit
# Register your models here.
admin.site.register(Boutique)
admin.site.register(Produit)