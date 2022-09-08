from django.db import models
from helpers.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"

    def __str__(self):
        return self.name


class Model(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Modellar"

    def __str__(self):
        return self.name


class Household(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    descriptions = models.TextField()
    model = models.ForeignKey(Model,on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Maishiy Texnika"
        verbose_name_plural = "Maishiy Texnikalar"

    def __str__(self):
        return self.name
