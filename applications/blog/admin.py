from django.contrib import admin
from django import forms
from .models import Post, Tag


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "tags": forms.CheckboxSelectMultiple,  # ✔ se ve como lista de checks
        }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ("title", "published_at", "is_published")
    list_filter = ("is_published", "published_at", "tags")
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("published_at", "updated_at")
