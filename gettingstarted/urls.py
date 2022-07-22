from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import routes.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", routes.views.index, name="index"),
    path("admin/", admin.site.urls),
    path("getRoutes/", routes.views.routes, name="routes"),
    path("getRouteById/", routes.views.route_id, name="route"),
    path("getPoi/", routes.views.poi, name="poi"),
    path("getPoiById/", routes.views.poi_id, name="poi_id"),
]
