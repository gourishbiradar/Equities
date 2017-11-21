from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Home', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    #url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #    views.activate, name='activate'),
    url(r'^DashBoard/$',views.DashBoard,name='DashBoard'),
    url(r'^History/$',views.History,name="History"),
    url(r'^InvFuture/$',views.FutureInv,name="FutureInv"),
    url(r'^InvOption/$',views.OptionInv,name="OptionInv"),
    url(r'^SectorwisePerformances/$',views.SectorwisePerformances,name="SectorwisePerformances"),
    url(r'^MostVolatileDeriavatives/$',views.MostVolatileDeriavatives,name="MostVolatileDeriavatives"),
    url(r'^SpecificDeriavatives/$',views.SpecificDeriavatives,name="SpecificDeriavatives"),
    url(r'^AboutUs/$',views.AboutUs,name="AboutUs"),
    url(r'^ContactUs/$',views.ContactUs,name="ContactUs"),
    #url(r'^DisplayFutures/$',views.DisplayFutures,name="DisplayFutures"),
    #url(r'^DisplayOptions/$',views.DisplayOptions,name="DisplayOptions"),
]
