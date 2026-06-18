from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import UserProfile, City, Property, Images, Booking, Review, Favorite, FavoriteItem , Amenity


admin.site.register(Review)
admin.site.register(City)
admin.site.register(Booking)
admin.site.register(UserProfile)
admin.site.register(Favorite)
admin.site.register(FavoriteItem)
admin.site.register(Amenity)


class ImagesInlines(admin.TabularInline):
    model = Images
    extra = 3

# class AmenityInlines(admin.TabularInline):
#     model = Amenity
#     extra = 1

@admin.register(Property)
class PropertyAdmin(TranslationAdmin):
    inlines = [ImagesInlines] #, AmenityInlines
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
