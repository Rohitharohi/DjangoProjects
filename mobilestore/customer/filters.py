import django_filters
from mobile.models import Mobile

class MobilesFilter(django_filters.FilterSet):
    class Meta:
        model=Mobile
        fields=["mobile_name","ram","color","price"]