from django.shortcuts import render,redirect # type: ignore
from .models import SiteConfig, HeroSection, HighlightSection, HowItWorksStep

from .models import CommunitySection
from .models import PracticeSection

# def home(request):
#     site_config = SiteConfig.objects.first()
#     hero = HeroSection.objects.prefetch_related('avatars').first()
#     highlights = HighlightSection.objects.all()
#     how_it_works_steps = HowItWorksStep.objects.all()
#     practices = PracticeSection.objects.all()
#     community_section = CommunitySection.objects.first()

#     context = {
#         'site_config': site_config,
#         'hero': hero,
#         'highlights': highlights,
#         'how_it_works_steps': how_it_works_steps,
#         'practices': practices,
#          "community_section": community_section,
#     }

#     return render(request, "home/home.html", context)


from .models import (
    SiteConfig, HeroSection, HighlightSection, HowItWorksStep,
    CommunitySection, PracticeSection, DashboardUser, DashboardStat
)

def home(request):
    site_config = SiteConfig.objects.first()
    hero = HeroSection.objects.prefetch_related('avatars').first()
    highlights = HighlightSection.objects.all()
    how_it_works_steps = HowItWorksStep.objects.all()
    practices = PracticeSection.objects.all()
    community_section = CommunitySection.objects.first()
    dashboard_user = DashboardUser.objects.first()
    dashboard_stats = DashboardStat.objects.all()

    context = {
        "site_config": site_config,
        "hero": hero,
        "highlights": highlights,
        "how_it_works_steps": how_it_works_steps,
        "practices": practices,
        "community_section": community_section,
        "dashboard_user": dashboard_user,
        "dashboard_stats": dashboard_stats,
    }

    return render(request, "home/home.html", context)










from django.contrib.auth import login   # type: ignore
from .forms import RegisterForm
from .models import RegisterPage

def register_view(request):
    register_page = RegisterPage.objects.first()

    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # save user
            login(request, user)  # auto-login
            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {
        "form": form,
        "register_page": register_page,
    })


from django.contrib.auth import authenticate, login  # type: ignore

from .models import LoginPage
from django.contrib.auth.models import User   # type: ignore

def login_view(request):
    login_page = LoginPage.objects.first()
    error = None

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user:
            login(request, user)
            return redirect("home")
        else:
            error = "Invalid email or password."

    return render(request, "login/login.html", {"login_page": login_page, "error": error})


from django.contrib.auth import logout  # type: ignore
from django.shortcuts import redirect   # type: ignore

def logout_view(request):
    logout(request)
    return redirect("login")



# app/views.py

from .models import PartnerHero, PartnerContact, PartnerFeature

def become_partner(request):
    hero = PartnerHero.objects.first()
    contact = PartnerContact.objects.first()
    features = PartnerFeature.objects.all()
    return render(request, 'partner/become_partner.html', {
        'hero': hero,
        'contact': contact,
        'features': features
    })


# About View


from .models import AboutSection

def about(request):
    sections = AboutSection.objects.filter(is_active=True).order_by("order")
    return render(request, "about/about.html", {"sections": sections})


#blog

from trading_app.models import BlogIntroSection, BlogPost
from collections import defaultdict

def blog_view(request):
    blog_intro = BlogIntroSection.objects.first()

    posts_by_category = defaultdict(list)
    posts = BlogPost.objects.order_by('created_at')
    for post in posts:
        posts_by_category[post.category].append(post)

    # convert defaultdict to regular dict
    posts_by_category = dict(posts_by_category)

    return render(request, "blog/blog.html", {
        "blog_intro": blog_intro,
        "blog_posts": posts_by_category,
    })



#footer components

from django.shortcuts import render

def faq(request):
    return render(request, 'footercomponents/faq.html')

def market_explore(request):
    return render(request, 'footercomponents/market_explore.html')

def ready_token(request):
    return render(request, 'footercomponents/ready_token.html')

def main_option(request):
    return render(request, 'footercomponents/main_option.html')

def file_checking(request):
    return render(request, 'footercomponents/file_checking.html')

def docs(request):
    return render(request, 'footercomponents/docs.html')

def press_kit(request):
    return render(request, 'footercomponents/press_kit.html')

def trade_investor(request):
    return render(request, 'footercomponents/trade_investor.html')