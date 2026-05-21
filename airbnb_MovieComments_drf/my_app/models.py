from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator


USER_ROLE = (
    ('guest', 'guest'),
    ('owner', 'owner'))

PROPERTY_TYPE = (
    ('apartment', 'apartment'),
    ('house', 'house'),
    ('studio', 'studio'))

RULES = (
    ('no_smoking', 'no_smoking'),
    ('pets_allowed', 'pets_allowed'),
    ('wi-fi', 'wi-fi'),
    ('etc', 'etc'))

STATUS = (
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('rejected', 'rejected'),
    ('cancelled', 'cancelled'))

class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(choices=USER_ROLE, default='guest')
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    account_created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}, {self.role}, {self.phone_number}'

class City(models.Model):
    city = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f'{self.city}'

class Property(models.Model):
    title = models.CharField(max_length=500, unique=True)
    description = models.TextField()
    price_per_night = models.PositiveIntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=500)
    property_type = models.CharField(choices=PROPERTY_TYPE, default='apartment')
    rules = MultiSelectField(max_length=200, choices=RULES, max_choices=4)
    max_guests = models.PositiveIntegerField(choices=[(i, str(i))for i in range(1, 15)], blank=True, null=True)
    bedrooms = models.PositiveIntegerField(choices=[(i, str(i))for i in range(1, 7)], blank=True, null=True)
    bathrooms = models.PositiveIntegerField(choices=[(i, str(i))for i in range(1, 7)], blank=True, null=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="properties")

    def __str__(self):
        return f'{self.title}, {self.city}, {self.property_type}, {self.price_per_night}$'

    def get_avg_rating(self):
        rating=self.reviews_set.all()
        if rating.exists():
            return round(sum([i.rating for i in rating]) / rating.count(),1)
        return 0

    def get_count_reviews(self):
        return self.reviews_set.count()

class Images(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images_set')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f'{self.property}, {self.image}'

class Booking(models.Model):
    count_person = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(14)], default=1)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    status = models.CharField(choices=STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guest}, {self.property}, {self.status}'

class Review(models.Model):
    rating = models.PositiveIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews_set')
    guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.guest}, {self.property}, {self.rating}, {self.comment}'

class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.favorite}, {self.property}'

class Amenity(models.Model):
    name_amenity = models.CharField(max_length=100)
    icon_amenity = models.FileField(upload_to='amenities_icons/', null=True, blank=True)
    property = models.ManyToManyField(Property, related_name='amenity_set')

    def __str__(self):
        return f'{self.name_amenity}, {self.icon_amenity}'





# ушуларды кошуш керек:
    # пользователь:
        # Оставить отзыв на жильё после завершённого бронирования.
        # История бронирований пользователья
        # Просмотр входящих запросов на аренду.
        # Бронирование доступных объектов.

    # owner
        # Активация/деактивация объектов.
        # Просмотр и управление бронированиями. (хост подтверждает/отказ) а путь bookings должен показать статус ожидание/забронирован/отказ

    # Функции для администраторов
        # Управление пользователями:
            # Блокировка и удаление аккаунтов.
        # Модерация объявлений:
            # Проверка и одобрение объектов.
        # Статистика:
            # Просмотр количества активных бронирований, пользователей, доходов и популярных локаций.
