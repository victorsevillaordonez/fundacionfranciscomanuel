from django.urls import path
from home import views
from django.conf.urls import url


urlpatterns = [
	path('history.html',views.history_view),
	url(r'^eventos/$', views.EventoListView.as_view(), name='allLista'),
	url(r'^lista_eventos/$', views.EventoAnteriorListView.as_view(), name='lista'),
	url(r'^lista_eventos_futuros/$', views.EventoFuturoListView.as_view(), name='listafuturoevento'),
    url(r'^ver_imagenes/(?P<evento_id>\d+)$', views.Ver_imagenes_view.as_view(), name='ver_imagenes'),
	url(r'^crear_evento/$', views.CreateEventView.as_view(), name='nuevo'),
	url(r'^editar/(?P<pk>\d+)$', views.UpdateEventoView.as_view(), name='editar'),
	url(r'^eliminar/(?P<pk>\d+)$', views.DeleteEventoView.as_view(), name='eliminar'),
	path('login/',views.login_view,name='login_view'),
	path('logout/', views.logout_view,name='logout_view'),
	path('', views.menu_view,name='menu_view'),
	url(r'^upload/$', views.UploadImageView.as_view(), name='upload'),


]