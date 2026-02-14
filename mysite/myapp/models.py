from django.db import models

# Create your models here.
class Item(models.Model):
    
    def _str_(self):
        return self.item_name
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField()
    item_price = models.IntegerField()
    item_image = models.CharField( max_length=500,default ="https://images.pexels.com/photos/958545/pexels-photo-958545.jpeg?cs=srgb&dl=pexels-chan-walrus-958545.jpg&fm=jpg")
