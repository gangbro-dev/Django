from django.contrib import admin
<<<<<<< HEAD
from .models import Article

# Register your models here.
admin.site.register(Article)
=======
from .models import Article, Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
>>>>>>> 453aefd82c356c5398bc0fedd06718d41e3455c2
