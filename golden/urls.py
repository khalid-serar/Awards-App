from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url('register/',views.signup, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/',auth_views.LogoutView.as_view(), name='logout'),
    url('profile/', views.profile, name='profile'),
    url('upload/',views.project,name='add_project'),
    url(r'^project_details/(?P<id>\d+)', views.project_view, name='projectdetails'),
    url(r'^review/(?P<project_id>\d+)', views.review_project, name='review'),
    url('search/', views.search_project, name='search'),
    url('api/projects',views.ProjectList.as_view(),name='projectsEndpoint'),
    url('api/profiles',views.ProfileList.as_view(),name='profilesEndpoint'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)