from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.template.defaultfilters import slugify
from django.urls import reverse
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='name')
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=2000)
    slug = models.SlugField(max_length=2000, null=False)

    def get_absolute_url(self):
        return reverse('register:profile', kwargs={'slug': self.slug})

    def get_absolute_url_detail(self):
        return reverse('register:profile_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username

class StatisticalUser(models.Model):
    amout = models.IntegerField()
    data_create = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.data_create.year) + str("-") + str(self.data_create.month)


class LoginAttempts(models.Model):
    customer = models.ForeignKey(User, null =True,blank=True, on_delete=models.CASCADE)
    th = models.AutoField(primary_key=True,blank=True)
    start  = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField( null=True,blank=True)