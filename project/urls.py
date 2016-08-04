from django.conf.urls import include, url
from django.contrib import admin

from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
  #  url(r'^class_based_view/', views.GetPost.as_view()),
    # class based views
    url(r'^state_list_class_view/', views.StateListView.as_view()),
    url(r'^state_detail_class_view/(?P<pk>\d+)/', views.StateDetailView.as_view()),

    #form view
    url(r'^city_search/','app.views.city_search'),

    #form- post view
    url(r'^city_search_post/','app.views.city_search_post'),

    #Create
    url(r'^create_city/', 'app.views.create_city'),
    url(r'^create_state/', 'app.views.create_state'),

    #edit views
    url(r'^edit_city/(?P<pk>\d+)/$','app.views.edit_city', name='edit_city'),
    url(r'^edit_state/(?P<pk>\d+)/$', 'app.views.edit_state'),

    #Delete views
    url(r'^delete_city/(?P<pk>\d+)/$','app.views.delete_city'),
    url(r'^delete_state/(?P<pk>\d+)/$', 'app.views.delete_state'),

    url(r'^city_list_class_view/', views.CityListView.as_view()),
    url(r'^city_detail_class_view/(?P<pk>\d+)/', views.CityDetailView.as_view()),


	 
    

     

     url(r'^state_list/', 'app.views.stateslist'),
     url(r'^city_list/','app.views.city_list'),
     url(r'^city_detail/(?P<pk>\d+)/', 'app.views.city_detail'),
     url(r'^state_detail/(?P<pk>\d+)/', 'app.views.state_detail'),
     url(r'^statecapital_list/', 'app.views.statecapital_list'),
     url(r'^statecapital_detail/(?P<pk>\d+)/', 'app.views.statecapital_detail'),

    url(r'^list/', 'app.views.list'),
    url(r'^detail/(?P<pk>\d+)/', 'app.views.detail'),
    url(r'^template_view2/', 'app.views.template_view2'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^template_view/', 'app.views.template_view'),

	url(r'^form_view/', 'app.views.form_view'),
	url(r'^get_post/','app.views.get_post'),
#	url(r'^get_post/','app.views.get_post'),

	# url(r'^first_view/$', 'app.views.first_view'),
	# url(r'^state_list/(?P<letter>\w+)/(?P<sort>\w+)', 'app.views.state_list')


]
