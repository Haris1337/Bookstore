from django.conf.urls import url

from . import views

app_name = 'book'

urlpatterns = [
	url(r'^books/$', views.book_list, name='list'),
	url(r'^purchase/(?P<id>[0-9]+)/$', views.purchase, name='purchase'),
	url(r'^login/$', views.login_view, name="login"),
	url(r'^logout/$', views.logout_view, name="logout"),
	url(r'^signup/$', views.signup_view, name="signup"),
	url(r'^add/$', views.add_view, name="add"),

]
