from django.contrib import admin
from django import forms

from .models import Post
from photos.models import Photo


class PhotoAdminForm(forms.ModelForm):
	class Meta:
		model = Photo
		fields = ['image', 'title', 'tags', 'description', 'is_featured']
		widgets = {
			'image': forms.FileInput(attrs={
				'style': 'width: 180px;'
			}),
			'title': forms.TextInput(attrs={
				'placeholder': 'Enter title (optional)',
				'style': 'width: 300px;'
			}),
			'tags': forms.TextInput(attrs={
				'placeholder': 'A comma-separated list of tags (optional)',
				'style': 'width: 300px;'
			}),
			'description': forms.Textarea(attrs={
				'placeholder': 'Add a short photo description that will be displayed below the photo on the post (optional)',
				'rows': 2,
				'cols': 50
			}),
		}


class PostPhotoAdmin(admin.TabularInline):
	model = Photo
	form = PhotoAdminForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	inlines = [PostPhotoAdmin]
	fields = [('title', 'author', 'status',), 'text', ('tags', 'slug')]
	list_display = ('title', 'status', 'created_on')
	list_filter = ("status",)
	search_fields = ['title', 'text']
	prepopulated_fields = {'slug': ('title',)}

	class Meta:
		model = Post
