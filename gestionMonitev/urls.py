from django.conf.urls import url
from gestionMonitev import views, models
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.base, name='base'),
    #Welcome
    url(r'^welcome/$', views.WelcomeListView.as_view(), name='index'),
    #ENRUTAMIENTO PARA EMPRESAS
    #List
    url(r'^empresa/$', views.EmpresaListView.as_view(), name='empresa-list'),
    #Detail
    url(r'^empresa/(?P<pk>\d+)/detail/$', views.EmpresaDetailView.as_view(), name='empresa-detail'),
    #Update
    url(r'^empresa/(?P<pk>\d+)/update/$', views.EmpresaUpdate.as_view(),name='empresa-update'),
    #Create
    url(r'^empresa/create/$', views.EmpresaCreate.as_view(), name='empresa-create'),
    #Delete
    url(r'^empresa/(?P<pk>\d+)/delete/$', views.EmpresaDelete.as_view(), name='empresa-delete'),

    #ENRUTAMIENTO PARA PASARELAS
    #List
    url(r'^pasarela/$', views.PasarelaListView.as_view(), name='pasarela-list'),
    #Detail
    url(r'^pasarela/(?P<pk>\d+)/detail/$', views.PasarelaDetailView.as_view(), name='pasarela-detail'),
    #Update
    url(r'^pasarela/(?P<pk>\d+)/update/$', views.PasarelaUpdate.as_view(),name='pasarela-update'),
    #Create
    url(r'^pasarela/create/$', views.PasarelaCreate.as_view(), name='pasarela-create'),
    #Delete
    url(r'^pasarela/(?P<pk>\d+)/delete/$', views.PasarelaDelete.as_view(), name='pasarela-delete'),

    #ENRUTAMIENTO PARA MEDIDORES
    #List
    url(r'^medidor/$', views.MedidorListView.as_view(), name='medidor-list'),
    #Detail
    url(r'^medidor/(?P<pk>\d+)/detail/$', views.MedidorDetailView.as_view(), name='medidor-detail'),
    #Update
    url(r'^medidor/(?P<pk>\d+)/update/$', views.MedidorUpdate.as_view(),name='medidor-update'),
    #Create
    url(r'^medidor/create/$', views.MedidorCreate.as_view(), name='medidor-create'),
    #Delete
    url(r'^medidor/(?P<pk>\d+)/delete/$', views.MedidorDelete.as_view(), name='medidor-delete'),

    #ENRUTAMIENTO PARA USUARIOS DEL  SISTEMA
    #List
    url(r'^user/$', views.UserListView.as_view(), name='user-list'),
    #Detail
    url(r'^user/(?P<pk>\d+)/detail/$', views.UserDetailView.as_view(), name='user-detail'),
    #Update
    url(r'^user/(?P<pk>\d+)/update/$', views.UserUpdate.as_view(),name='user-update'),
    #Create
    url(r'^user/create/$', views.UserCreate.as_view(), name='user-create'),
    #Delete
    url(r'^user/(?P<pk>\d+)/delete/$', views.UserDelete.as_view(), name='user-delete'),
    #Graphic
    url(r'^graphic/$',views.empresas,name='empresas'),
    #pruebas graficas estaticas
    url(r'^graphic/$',views.get_data, name='grafica'),
    #Prueba de graficas con datos reales
    #url(r'^graphic/$',views.get_data_variable, name='prueba-grafica'),
]