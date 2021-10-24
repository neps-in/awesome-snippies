# File: thanks/admin.py

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Thanks

# Great Trick to get foreign related items using FK of related models
def catalog_title(object):
  return object.catalog.title

class ThanksAdmin(admin.ModelAdmin):
    # To display catalog_title along with thanks counter in thanks admin page, 

    list_display = ('id', catalog_title,
	'thanks_counter','created_on',
    'updated_on','status')


admin.site.register(Thanks, ThanksAdmin)

# File: thanks/models.py

from django.db import models

# from catalog.models import Catalog

# Thanks counter
# Say thank you to a book, Products that changed your life.
# Step in increase of 50

class Thanks(models.Model):

	id = models.BigAutoField(primary_key=True)

    # Foreign Key to Catalog
	catalog = models.ForeignKey(Catalog, related_name='thanks', on_delete=models.CASCADE,blank=False, default='')
	thanks_counter = models.BigIntegerField(default='0')
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=True)
