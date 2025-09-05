from django.urls import path
from . import views
from .views import become_partner

urlpatterns = [
    path("", views.home, name="home"),
    
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path('become-partner/', become_partner, name='become_partner'),
    path("about/", views.about, name="about"),
    path("blog/", views.blog_view, name="blog"),

    path('faq/', views.faq, name='faq'),
    path('market-explore/', views.market_explore, name='market_explore'),
    path('ready-token/', views.ready_token, name='ready_token'),
    path('main-option/', views.main_option, name='main_option'),
    path('file-checking/', views.file_checking, name='file_checking'),
    path('docs/', views.docs, name='docs'),
    path('press-kit/', views.press_kit, name='press_kit'),
    path('trade_investor/', views.trade_investor, name='trade_investor'),
    

]