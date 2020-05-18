from django.contrib import admin
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.FresherRigister,name="FresherRigister"),
    path('FresherRigister',views.FresherRigister,name="FresherRigister"),
    path('CompanyRegister',views.CompanyRegister,name="CompanyRegister"),
    path('Login',views.Login,name='Login'),
    path('fresherdata/(?P<User_id>[0-9]+)/$',views.fresherdata,name='fresherdata'),
    path('FreshExtradata',views.FreshExtradata,name='FreshExtradata'),
    path('ProfileData/(?P<User_id>[0-9]+)/$',views.ProfileData,name='ProfileData'),
    path('Companyprofile_data/(?P<User_id>[0-9]+)/$',views.Companyprofile_data,name='Companyprofile_data'),
    path('Support_Course/(?P<User_id>[0-9]+)/$',views.Support_Course,name='Support_Course'),
    path('load_Course',views.load_Course,name='load_Course'),
    path('mulltisearch/(?P<idd>.*)',views.mulltisearch,name='mulltisearch'),
    path('country_list',views.country_list,name='country_list'),
    path('fresherqualification/(?P<User_id>[0-9]+)/$',views.fresherqualification,name="fresherqualification"),
    path('fresherqualificationextra',views.fresherqualificationextra,name="fresherqualificationextra"),
    path('Profiledef/(?P<User_id>[0-9]+)/$',views.Profiledef,name='Profiledef'),
    path('Profileextradef',views.Profileextradef,name='Profileextradef'),
    path('job_postview',views.job_postview,name='job_postview'),
    # path('job_applied',views.job_applied,name='job_applied'),
    path('Logout',views.Logout,name='Logout'),
    path(r'Apply_Click/(?P<idd>.*)',views.Apply_Click,name='Apply_Click'),
    path(r'Applied_Candidates/(?P<idd>.*)(?P<uidd>.*)',views.Applied_Candidates,name='Applied_Candidates'),
    path(r'candidate/(?P<idd>.*)(?P<uidd>.*)',views.candidate,name='candidate'),
    path('candidate_search',views.candidate_search,name='candidate_search'),
    path('studentlist', views.studentlist,name='studentlist'),
    path('Resume_Edite', views.Resume_Edite,name='Resume_Edite'),
    path('<int:sUser_id>/intenction/(?P<User_id>[0-9]+)/$', views.intenction,name='intenction'),
    path('User_intenction', views.User_intenction,name='User_intenction'),
    path(r'notification_read/(?P<idd>.*)(?P<uidd>.*)',views.notification_read,name='notification_read'),
    
]