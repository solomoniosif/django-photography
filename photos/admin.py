from django.contrib import admin

from photos.models import Category, Gallery, Album, Photo


class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


class GalleryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}


class AlbumAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'is_featured')
	list_editable = ('is_featured',)


class PhotoAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'tag_list', 'album', 'is_featured')
	list_editable = ('is_featured',)

	# Get list of tags
	def get_queryset(self, request):
		return super().get_queryset(request).prefetch_related('tags')

	@admin.display(description="Tags")
	def tag_list(self, obj):
		return u", ".join(o.name for o in obj.tags.all())


admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)