from django.urls import path
from . import views

urlpatterns = [
      path('details/',views.orgList,name="details"),
      path('profileOrg/<str:pk_value>/',views.org_profile,name="org_profile"),
      path('Createfeed/',views.createFeed,name="feed"),
      path('listFeed/',views.listFeed,name="listFeed"),
      path('search/',views.search,name="search"),
      path('newsFeed/<str:pk>/',views.newsFeed,name="newsFeed"),
      # path('PostComment',views.PostComment,name="PostComment"),
      path('updateFeed/<str:pk>',views.updateFeed,name="updateFeed"),
      path('deleteFeed/<str:pk>/',views.deleteFeed,name="deleteFeed"),
      path('account_setting/',views.account_set,name="account_setting"),
      path('register/',views.orgRegister,name="register"),
      path('mission/',views.mission,name="mission"),
      path('login/',views.user_login,name="login"),
      path('logout/',views.user_logout,name="logout"),    
]