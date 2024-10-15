from .views import login_user, signup,home,about,contact,shop,logout_user,product, category, update_user,update_password,update_profile, stk_push, index
from django.urls import path
app_name = 'shopingcentre'
urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup,name='signup'),
    path('login/', login_user,name='login'),
    path('logout/', logout_user,name='logout'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('product/<int:pk>', product, name='product'),   
    path('category/<str:foo>', category, name='category'),
    path('update_user/', update_user   ,name='update_user'),
    path('update_password/', update_password   ,name='update_password'),
    path('update_profile/', update_profile   ,name='update_profile'),
    path('checkout/', index, name='checkout'),
    path('stk_push/', stk_push, name='stk_push'),
]
