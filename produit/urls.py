from django.conf.urls import url
from . import views
app_name = 'boutique'
urlpatterns=[




    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),


    url(r'^create_boutique/$', views.create_boutique, name='create_boutique'),
    url(r'^$', views.index, name='index'),
    url(r'^produits/(?P<filter_by>[a-zA_Z]+)/$', views.produits, name='produits'),
    url(r'^(?P<boutique_id>[0-9]+)/create_produit/$', views.create_produit, name='create_produit'),
    url(r'^(?P<boutique_id>[0-9]+)/delete_produit/(?P<produit_id>[0-9]+)/$', views.delete_produit, name='delete_produit'),
    url(r'^(?P<boutique_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<produit_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^(?P<produit_id>[0-9]+)/smile/$', views.smile, name='smile'),
    url(r'^(?P<boutique_id>[0-9]+)/delete_boutique/$', views.delete_boutique, name='delete_boutique'),
    url(r'^vosproduit/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail_produit'),
    url(r'^activer/(?P<produit_id>[0-9]+)/$', views.Activer, name='activer'),
    url(r'^desactiv/(?P<produit_id>[0-9]+)/$', views.DesActiver, name='desactiver'),
    url(r'^produits/$', views.post_list, name='post_list'),
    url(r'^categorie/$', views.Categorie, name='Categorie'),

]

