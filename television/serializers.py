from rest_framework import serializers
from .models import Television,Category,Model

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'
        

class TelevisionSerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    class Meta:
        model = Television
        fields = '__all__'