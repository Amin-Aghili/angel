from django.contrib import admin
from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'created', 'updated')
    list_editable = ('price',)
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('category',)
    actions = ('make_available', 'make_unavailable')

    @staticmethod
    def make_available(self, request, queryset):
        rows = queryset.update(available=True)
        self.message_user(request, f'{rows} rows updated')
    make_available.short_description = 'Make available'

    @staticmethod
    def make_unavailable(self, request, queryset):
        rows = queryset.update(available=False)
        self.message_user(request, f'{rows} rows updated')
    make_unavailable.short_description = 'Make unavailable'