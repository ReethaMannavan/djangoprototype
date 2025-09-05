from django.contrib import admin  # type: ignore

# Register your models here.

from .models import SiteConfig

admin.site.register(SiteConfig)



from .models import HeroSection, HeroAvatar

class HeroAvatarInline(admin.TabularInline):
    model = HeroAvatar
    extra = 5  # default 5 avatars

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    inlines = [HeroAvatarInline]
    list_display = ('heading', 'subheading', 'created_at')


# core/admin.py

from .models import HighlightSection

@admin.register(HighlightSection)
class HighlightSectionAdmin(admin.ModelAdmin):
    # Only show the fields you want to fill dynamically
    list_display = ('id',)
    fieldsets = (
        ('Top Section', {
            'fields': ('center_image',)
        }),
        ('Left Column Content', {
            'fields': ('content', 'paragraph_left', 'paragraph_right')
        }),
        ('Right Column Image', {
            'fields': ('right_image',)
        }),
    )



from .models import HowItWorksStep

@admin.register(HowItWorksStep)
class HowItWorksAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)   # allows reordering directly in list view




from .models import CommunitySection

@admin.register(CommunitySection)
class CommunitySectionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    fieldsets = (
        ("Content", {
            "fields": ("title", "description")
        }),
        ("Images", {
            "fields": (
                ("image1", "alt1"),
                ("image2", "alt2"),
                ("image3", "alt3"),
                ("image4", "alt4"),
                ("image5", "alt5"),
            )
        }),
    )





from .models import PracticeSection

@admin.register(PracticeSection)
class PracticeSectionAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'highlight')
    list_editable = ('highlight',)
    ordering = ('number',)
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': ('number', 'title', 'highlight')
        }),
        ('Optional Details', {
            'fields': ('description', 'button_text', 'button_link'),
        }),
    )




# app/admin.py

from .models import PartnerHero, PartnerContact, PartnerFeature

admin.site.register(PartnerHero)
admin.site.register(PartnerContact)
admin.site.register(PartnerFeature)



#about
from .models import AboutSection, AboutFeature


class AboutFeatureInline(admin.TabularInline):
    model = AboutFeature
    extra = 1  # show one empty row by default


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "kind", "order", "is_active")
    list_filter = ("kind", "is_active")
    search_fields = ("title", "subtitle", "body")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("order",)
    inlines = [AboutFeatureInline]


@admin.register(AboutFeature)
class AboutFeatureAdmin(admin.ModelAdmin):
    list_display = ("headline", "section")
    search_fields = ("headline", "description")



#blog


from .models import BlogIntroSection

@admin.register(BlogIntroSection)
class BlogIntroSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "highlight_title", "highlight_word")


#blog categories

from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')








from .models import RegisterPage, LoginPage

@admin.register(RegisterPage)
class RegisterPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

@admin.register(LoginPage)
class LoginPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')



# Dashboard




from .models import DashboardUser, DashboardStat

@admin.register(DashboardUser)
class DashboardUserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

@admin.register(DashboardStat)
class DashboardStatAdmin(admin.ModelAdmin):
    list_display = ("title", "value", "change", "change_type")

