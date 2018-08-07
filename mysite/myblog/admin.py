from django.contrib import admin
from myblog.models import Post
from myblog.models import Category


# admin.site.register(Category)
# admin.site.register(Post)



class CatergoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CatergoryInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts',]