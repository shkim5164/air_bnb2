from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin"""

    list_display = (
        "name", "used_by"
    )
    def used_by(self,obj):
        return obj.rooms.count()
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """Room Admin"""

    fieldsets = (
        (
            "Basic Info",
            {"fields" : ("name", "description", "country", "address", "price")}
        ),
        (   "Times",
            {"fields" : ("check_in", "check_out", "instant_book")}
        ),
        (   "Spaces",
            {"fields" : ("guests",)}
        ),
        (   "More About The Space",
            {"fields" : ("amenities",),
            "classes" : ("collapse",)},
            
        ),
        ("Last Details",
        {
            "fields" : ("host",)
        })
    )
    list_display=(
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "count_amenities",
        "count_photos"
    )

    ordering = ('name', 'price')
    
    list_filter = ("host__superhost","instant_book", "city", "country")

    search_fields = ("=city", "^host__username")

    filter_horizontal = ( "amenities",)
    
    def count_amenities(self, obj):
        #print(obj.amenities.count())
        return obj.amenities.count()

    def count_photos(self, obj):
        #print(obj.amenities.count())
        return obj.photos.count()


#    count_amenities.short_description = 'New'

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
