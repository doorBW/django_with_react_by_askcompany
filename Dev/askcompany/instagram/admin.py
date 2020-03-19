from django.contrib import admin
from .models import Post, Comment
from django.utils.safestring import mark_safe

# Register your models here.
# 방법1
#admin.site.register(Post)

# 방법2
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)

# 방법3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','photo_tag', 'message', 'message_length','is_public', 'created_at', 'updated_at']
    list_display_links = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px"/>')
        return None

    def message_length(self, post):
        return len(post.message)

    search_fields = ['message']
    list_filter = ['created_at', 'is_public']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass