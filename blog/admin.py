from django.contrib import admin

from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'slug']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug',
                    'date_added','date_updated','created_by')
    list_filter = ('active','created_by','categories')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'slug','description','body','keywords']
    fields = ('title','slug','categories','description','keywords','body',
              'active')

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()


admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)