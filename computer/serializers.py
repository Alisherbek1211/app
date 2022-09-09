from rest_framework import serializers
from .models import Computer,Category,Model

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
        
class ModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'


class ComputerSerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only=True)
    class Meta:
        model = Computer
        fields = '__all__'