from django.db import models


class Branch(models.Model):
    class Meta:
        verbose_name = 'branch'
        verbose_name_plural = 'branches'
    
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name
    

class Group(models.Model):
    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'
    
    name = models.CharField(max_length=100, null=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Student(models.Model):
    
    MALE = 'male'
    FEMALE = 'female'
    
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
    
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=300, null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default=MALE)


    def __str__(self):
        return self.name
