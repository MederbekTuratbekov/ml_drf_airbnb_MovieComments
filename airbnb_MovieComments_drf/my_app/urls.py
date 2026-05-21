from django.urls import path
from .views import RegisterView, CustomLoginView, LogoutView
from .views import (UserProfileAPIView, UserProfileUpdateAPIView, PropertyListAPIView,
                    PropertyDetailAPIView, BookingListAPIView, BookingCreateAPIView,
                    ReviewCreateAPIView, FavoriteItemListAPIView, PropertyUpdateAPIView,
                    PropertyCreateAPIView)


urlpatterns = [
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),

    path('profile/', UserProfileAPIView.as_view(), name = 'profile'),
    path('profile_update/', UserProfileUpdateAPIView.as_view(), name = 'update_profile'),

    path('', PropertyListAPIView.as_view(), name = 'property_list'),
    path('property_create/', PropertyCreateAPIView.as_view(), name = 'property_list'),
    path('<int:pk>/', PropertyDetailAPIView.as_view(), name = 'property_details'),
    path('property_update/<int:pk>/', PropertyUpdateAPIView.as_view(), name = 'property_update'),

    path('bookings/', BookingListAPIView.as_view(), name='booking_list'),
    path('booking_create/', BookingCreateAPIView.as_view(), name='bookings'),

    path('review_create/', ReviewCreateAPIView.as_view(), name = 'create_review'),

    path('favorites/', FavoriteItemListAPIView.as_view(), name = 'favorite_list'),
]
