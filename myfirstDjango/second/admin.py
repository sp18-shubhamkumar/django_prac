from django.contrib import admin
from .models import secondary, store, softwareReviews, secondCertify
# Register your models here.
class secondReviewinline(admin.TabularInline):
    model=softwareReviews
    extra=2

class secondVariety(admin.ModelAdmin):
    list_display=('name','type')
    inlines=[secondReviewinline]

class storeadmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('second_variety',)

class secondCertificateAdmin(admin.ModelAdmin):
    list_display=('second','certificate_number')

admin.site.register(secondary,secondVariety)
admin.site.register(store,storeadmin)
admin.site.register(secondCertify,secondCertificateAdmin)
# admin.site.register(softwareReviews,secondReviewinline)