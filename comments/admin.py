from django.contrib import admin
from .models import Comment, Reply

class ReplyInline(admin.TabularInline):
    model = Reply
    extra = 1  # Number of empty reply forms to display

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination', 'content', 'created_at', 'updated_at')
    search_fields = ('user__email', 'content')
    list_filter = ('created_at',)
    inlines = [ReplyInline]  # Allows adding replies directly in comment admin

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'content', 'created_at', 'updated_at')
    search_fields = ('user__email', 'content')
    list_filter = ('created_at',)

admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)
