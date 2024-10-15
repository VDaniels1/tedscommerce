from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Customers, Product, Orders, Category, Profile

# Register your models here.
admin.site.register(Customers)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(Category)
admin.site.register(Profile)

#mix profile infor and user info

class ProfileInline(admin.StackedInline):
    model = Profile
#extend user model
class CustomerUserAdmin(UserAdmin):
    model = User
    can_delete = False
    inlines=[ProfileInline]
    
#unregister the old way
admin.site.unregister(User)
#register the new way
admin.site.register(User, CustomerUserAdmin)


#register the new way
