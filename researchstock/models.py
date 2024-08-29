from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


USER_ROLES = {
    ('Admin', 'Admin'),
    ('Research Staff Member', 'Research Staff Member'),
    ('Supervisor', 'Supervisor'),
    ('Higher Approver', 'Higher Approver'),
    ('Order Manager', 'Order Manager'),
    ('Stock Manager', 'Stock Manager')
}

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userRole = models.CharField(choices=USER_ROLES, max_length=100, default="Research Staff Member")

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class UserRole(models.Model):
    role_id = models.IntegerField(default=0)
    role_name = models.CharField(max_length=50)

class Institute(models.Model):
    institute_id = models.IntegerField(default=0)
    institute_name = models.CharField(max_length=100)

class ResearchCenter(models.Model):
    center_id = models.CharField(max_length=10)
    center_name = models.CharField(max_length=100)
    institute_id = models.ForeignKey(Institute, on_delete=models.CASCADE, null=True, blank=True)

class Laboratory(models.Model):
    lab_id = models.CharField(max_length=10)
    lab_name = models.CharField(max_length=50)
    center_id = models.ForeignKey(ResearchCenter, on_delete=models.CASCADE, null=True, blank=True)

class StorageLocation(models.Model):
    storage_location_id = models.CharField(max_length=10)
    storage_location_name = models.CharField(max_length=50)
    location_id = models.ForeignKey(Laboratory, on_delete=models.CASCADE, null=True, blank=True)

class StorageLevel(models.Model):
    storage_level_id = models.IntegerField(default=0)
    storage_level = models.CharField(max_length=50)

class RiskCategory(models.Model):
    risk_category_id = models.IntegerField(default=0)
    risk_category = models.CharField(max_length=20)
    role_id = models.ForeignKey(StorageLevel, on_delete=models.CASCADE)

class Chemical(models.Model):
    chemical_id = models.CharField(max_length=10)
    common_name = models.CharField(max_length=50)
    systematic_name = models.CharField(max_length=50)
    risk_category = models.ForeignKey(RiskCategory, on_delete=models.CASCADE)

class OrderItem(models.Model):
    order_id = models.AutoField(primary_key=True)
    chemical_id = models.ForeignKey(Chemical, on_delete= models.CASCADE)
    required_amount = models.IntegerField(default=1)


DISPOSAL_STATUS = {
    ('NOT YET', 'Not yet'),
    ('DISPOSED', 'Disposed'),
}

# class StockItem(models.Model):
#     stock_id = models.CharField(max_length=10, null=False)
#     chemical_id = models.ForeignKey(Chemical, on_delete=models.CASCADE)
#     initial_stock = models.IntegerField(default=0)
#     Current_stock = models.IntegerField(default=0)
#     disposal_date = models.DateField(default=datetime.date.today)
#     disposal_status = models.CharField(choices=DISPOSAL_STATUS, default='Not yet')
#     storage_location = models.ForeignKey(StorageLocation, on_delete=models.CASCADE)
#     storage_level = models.ForeignKey(StorageLevel, on_delete=models.CASCADE)





