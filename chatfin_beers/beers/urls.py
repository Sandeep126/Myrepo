from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'user/$',
        views.user_creation,
        name='user_creation'
    ),
    url(
        r'beers/$',
        views.get_post_beers,
        name='get_post_beers'
    ),
    url(
        r'beers/(?P<pk>[0-9]+)$',
        views.get_delete_update_beers,
        name='get_delete_update_beers'
    ),
    url(
        r'beers/(?P<beer_name>[a-zA-Z0-9]+)$',
        views.get_beer_review,
        name='get_beer_review'
    ),
    url(
        r'review/$',
        views.rate_beer,
        name='rate_beer'
    ),

]