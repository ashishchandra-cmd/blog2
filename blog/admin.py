from django.contrib import admin
from blog.models import Post
# Register your models here.
class Adminpost(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','create','update','status','tags']
    list_filter=('author','title','status')
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','body')
    row_id_fields=('author',)
    date_hierarchy=('publish')
    ordering=['status','publish']

admin.site.register(Post,Adminpost)
#for comments
from blog.models import Comment
class CommentAdmin(admin.ModelAdmin):
    list_display=('post','name','email','body','created','updated','active')
admin.site.register(Comment,CommentAdmin)
