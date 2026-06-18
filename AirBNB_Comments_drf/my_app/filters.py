import django_filters
from .models import Property, City, PROPERTY_TYPE, RULES


class PropertyFilter(django_filters.FilterSet):
    price_per_night = django_filters.RangeFilter()  # Фильтр по диапазону цены за ночь
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all())  # Фильтр по городу
    property_type = django_filters.ChoiceFilter(choices=PROPERTY_TYPE)  # Используем PROPERTY_TYPE
    max_guests = django_filters.RangeFilter()  # Фильтр по количеству гостей
    bedrooms = django_filters.RangeFilter()  # Фильтр по количеству спален
    bathrooms = django_filters.RangeFilter()  # Фильтр по количеству ванных комнат
    is_active = django_filters.BooleanFilter()  # Фильтр по активности недвижимости
    rules = django_filters.MultipleChoiceFilter(choices=RULES)  # Используем RULES

    class Meta:
        model = Property
        fields = ['price_per_night', 'city', 'property_type', 'max_guests', 'bedrooms', 'bathrooms', 'is_active', 'rules']
