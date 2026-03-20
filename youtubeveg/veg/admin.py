from django.contrib import admin
from django.utils.html import format_html
from veg.models import Receipe  

class ReceipeAdmin(admin.ModelAdmin):
    list_display = ('receipe_name', 'receipe_description', 'image_tag', 'user')
    search_fields = ('receipe_name',)  
    
    def image_tag(self, obj):
        if obj.receipe_image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.receipe_image.url)
        return "No Image"
    
    image_tag.short_description = 'Image'
    

admin.site.register(Receipe, ReceipeAdmin)


# admin - newpassword123
