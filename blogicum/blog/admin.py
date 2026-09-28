from django.contrib import admin
from .models import Post, Category

# admin.site.register(Post)
# admin.site.register(Category)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    # list_editable = ('category', 'created_at')
    # search_fields = ('title', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('description',)
    list_editable = ('description',)
    search_fields = ('title', 'description')
