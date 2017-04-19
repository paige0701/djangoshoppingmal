from datetime import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(AbstractUser):
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    image = models.ImageField(blank=True)
    stock = models.PositiveIntegerField()
    status = models.IntegerField()
    description = models.TextField()
    views = models.PositiveIntegerField()
    likes = models.IntegerField()
    manufacturer = models.CharField(max_length=50)
    category = models.ForeignKey(Category)
    # comments = models.ForeignKey(Comment, blank=True, null=True)

    def __str__(self):
        return self.name


class Comment(models.Model):

    author = models.ForeignKey(User)
    content = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, related_name='comment', null=True, blank=True)

    def __str__(self):
        return self.author.email


class Cart(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    # product * quantity --> for one product or line
    def get_subtotal(self):

        price = self.product.price
        quantity = self.quantity
        subtotal = price * quantity

        return subtotal




