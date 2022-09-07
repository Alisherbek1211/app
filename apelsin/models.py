from django.db import models
from helpers.models import BaseModel

Ram_Choises = [
    ('4','4'),
    ('8','8'),
    ('12','12'),
]

Rom_Choices = [
    ('32','32'),
    ('64','64'),
    ('128','128'),
    ('256','256'),
]

class Category(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Phone(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    ram = models.CharField(choices=Ram_Choises,max_length=255,null=True,blank=True)
    rom = models.CharField(choices=Rom_Choices,max_length=255,null=True,blank=True)
    color = models.CharField(max_length=255)
    descriptions = models.TextField()

    class Meta:
        verbose_name = "Telefon va gadjetlar"
        verbose_name_plural = "Telefon va gadjetlar"

    def __str__(self):
        return self.name
