from typing import Any, List, Tuple
from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words!"

    parameter_name = "star"

    def lookups(self, request, model_admin):
        return [
            ("bad", "Bad"),
            ("good", "Good"),
        ]

    def queryset(self, request, reviews):
        star = self.value()
        if star == "bad":
            return reviews.filter(rating__lt=3)
        elif star == "good":
            return reviews.filter(rating__gte=3)
        else:
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
