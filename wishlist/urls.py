from django.urls import path, include
from wishlist.views import show_wishlist_ajax, login_user, show_json, show_json_by_id, show_wishlist, show_xml, register, login_user, logout_user


app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('wishlist-ajax', show_wishlist_ajax, name='wishlist-ajax')
]