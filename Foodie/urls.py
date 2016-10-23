"""Foodie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from FoodieApp.views import home
from FoodieApp.views import register
from FoodieApp.views import login_view
from FoodieApp.views import logout_view
from FoodieApp.views import restaurant_login_view
from FoodieApp.views import customerRestaurant_view
from FoodieApp.views import payment
from FoodieApp.views import editmenu
from FoodieApp.views import restaurantlist_view
from FoodieApp.views import successorder_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^register', register),
    url(r'^login', login_view),
    url(r'^logout', logout_view),
    url(r'^rlogin', restaurant_login_view),
    url(r'^payment', payment),
    url(r'^editmenu', editmenu),
    url(r'^RestaurantList/(?P<district_name>.*)/(?P<food_name>.*)/$',
        restaurantlist_view),
    url(r'^successorder', successorder_view),
    url(r'^customerRestaurant/(?P<res_id>\d+)/$', customerRestaurant_view),
]
