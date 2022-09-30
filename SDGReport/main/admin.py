from django.contrib import admin


from .models import Country, Goal, Indicator, Performance

# Register your models here.

admin.site.register(Country)
admin.site.register(Goal)
admin.site.register(Indicator)
admin.site.register(Performance)
