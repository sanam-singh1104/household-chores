from django.contrib import admin

from .models import Household, Roommate


@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Roommate)
class RoommateAdmin(admin.ModelAdmin):
    list_display = ("name", "household")
    list_filter = ("household",)
