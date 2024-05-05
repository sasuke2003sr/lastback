# from django.db import models

# class Delhi(models.Model):
#   firstname = models.CharField(max_length=255)
#   lastname = models.CharField(max_length=255)


from django.db import models

class Delhi(models.Model):
    firstname = models.CharField(max_length=255, verbose_name='First Name')
    lastname = models.CharField(max_length=255, verbose_name='Last Name')
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    class Meta:
        verbose_name_plural = 'Delhi Members'
        ordering = ['lastname', 'firstname']

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'
