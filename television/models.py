from django.db import models
from helpers.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    icon = models.ImageField()

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


class Television(BaseModel):
    name = models.CharField(max_length=255)
    image = models.ImageField()
    price = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    descriptions = models.TextField()
    model = models.ForeignKey(Model,on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Televizor"
        verbose_name_plural = "Televizorlar"

    def __str__(self):
        return self.name
