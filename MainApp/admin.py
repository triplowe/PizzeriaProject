from django.contrib import admin

# Register your models here.
from .models import Pizza
from .models import Topping
from .models import Comment
from .models import Image

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)
admin.site.register(Image)