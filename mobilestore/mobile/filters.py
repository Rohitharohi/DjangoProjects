import django_filters
from .models import Mobile

class MobileFilter(django_filters.FilterSet):
    class Meta:
        model=Mobile
        fields=["mobile_name","ram","color","price"]