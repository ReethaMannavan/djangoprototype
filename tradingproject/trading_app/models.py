from django.db import models # type: ignore

# Create your models here.



class SiteConfig(models.Model):
    logo = models.ImageField(upload_to='logos/')  

    def __str__(self):
        return f"SiteConfig {self.id}"  # or just return "Logo"


class HeroSection(models.Model):
    bg_image = models.ImageField(upload_to='hero_bg/')
    hero_image = models.ImageField(upload_to='hero_main/')
    subheading = models.CharField(max_length=255)
    heading = models.CharField(max_length=500)
    paragraph = models.TextField()

    avatar_text = models.CharField(max_length=255, blank=True, null=True)
    
    # Arrow section
    arrow_paragraph = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading


class HeroAvatar(models.Model):
    hero_section = models.ForeignKey(HeroSection, related_name='avatars', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hero_avatars/')
    

    def __str__(self):
        return f"Avatar for {self.hero_section.heading}"


# highlightsection/models.py

class HighlightSection(models.Model):
    # Remove number, title, order
    content = models.TextField("Top description")
    paragraph_left = models.TextField("Bottom left paragraph", blank=True)
    paragraph_right = models.TextField("Bottom right paragraph", blank=True)
    center_image = models.ImageField("Top center image", upload_to='highlights/', blank=True, null=True)
    right_image = models.ImageField("Right column image", upload_to='highlights/', blank=True, null=True)

    def __str__(self):
        return f"HighlightSection {self.id}"  # optional






class PracticeSection(models.Model):
    number = models.PositiveIntegerField("Step Number")
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description", blank=True, null=True)
    highlight = models.BooleanField("Highlight This Card?", default=False)
    button_text = models.CharField("Button Text", max_length=50, blank=True, null=True)
    button_link = models.CharField("Button Link", max_length=255, blank=True, null=True)


    class Meta:
        ordering = ['number']

    def __str__(self):
        return f"{self.number}. {self.title}"








class HowItWorksStep(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to="howitworks/")
    order = models.PositiveIntegerField(default=0)  # step order

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title




# community section 


class CommunitySection(models.Model):
    title = models.CharField(max_length=150, default="Build a Strong Community")
    description = models.TextField(default="Join a global network of passionate traders. Share strategies, learn from experts, and grow together in a supportive, success-driven environment.")

    # Images
    image1 = models.ImageField(upload_to="community/", blank=True, null=True)
    image2 = models.ImageField(upload_to="community/", blank=True, null=True)
    image3 = models.ImageField(upload_to="community/", blank=True, null=True)
    image4 = models.ImageField(upload_to="community/", blank=True, null=True)
    image5 = models.ImageField(upload_to="community/", blank=True, null=True)

    # Alt Texts for SEO
    alt1 = models.CharField(max_length=150, blank=True, null=True)
    alt2 = models.CharField(max_length=150, blank=True, null=True)
    alt3 = models.CharField(max_length=150, blank=True, null=True)
    alt4 = models.CharField(max_length=150, blank=True, null=True)
    alt5 = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Community Section"
        verbose_name_plural = "Community Sections"




# app/models.py


# Hero Section
class PartnerHero(models.Model):
    hero_image = models.ImageField(upload_to='partner_hero/')
   

    
    def __str__(self):
        return f"Hero Image {self.id}"


# Contact Info
class PartnerContact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return f"Contact Info {self.id}"


# Features Grid (2x2)
class PartnerFeature(models.Model):
    icon = models.ImageField(upload_to='partner_features/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title



#about

class AboutSection(models.Model):
    KIND_CHOICES = [
        ("hero", "Hero"),
        ("who", "Who We Are"),
        ("mission", "Mission"),
        ("vision", "Vision"),
        ("why_choose", "Why Choose TRACO"), 
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_kind_display()} - {self.title}"


class AboutFeature(models.Model):
    section = models.ForeignKey(
        AboutSection, related_name="features", on_delete=models.CASCADE
    )
    icon = models.ImageField(upload_to="about/features/", blank=True, null=True)
    headline = models.CharField(max_length=200, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.headline



# Blog



class BlogIntroSection(models.Model):
    title = models.CharField(max_length=255, help_text="Main heading before highlighted text")
    highlight_title = models.CharField(max_length=100, help_text="Highlighted text in neon green (e.g. Build Knowledge)")
    description = models.TextField(help_text="Paragraph under the heading")
    highlight_word = models.CharField(max_length=50, help_text="Highlighted word inside description (e.g. TRACO)")
    image = models.ImageField(upload_to='blog/intro/', help_text="Main oval image")
    icon1 = models.ImageField(upload_to='blog/intro/icons/', blank=True, null=True, help_text="Top-right decorative icon")
    icon2 = models.ImageField(upload_to='blog/intro/icons/', blank=True, null=True, help_text="Bottom-left decorative icon")

    class Meta:
        verbose_name = "Blog Intro Section"
        verbose_name_plural = "Blog Intro Section"

    def __str__(self):
        return f"Blog Intro - {self.highlight_title}"




#blog categories

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('stocks', 'Stocks'),
        ('mutual-funds', 'Mutual Funds'),
        ('personal-finance', 'Personal Finance'),
        ('futures-options', 'Futures & Options'),
    ]

    title = models.CharField(max_length=255)
    meta = models.CharField(max_length=255, help_text="E.g. '5 Mins Read · 20 May 2025'")
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title












class RegisterPage(models.Model):
    title = models.CharField(max_length=100, default="Register")
    image = models.ImageField(upload_to="register/", blank=True, null=True)

    class Meta:
        verbose_name = "Register Page"
        verbose_name_plural = "Register Page"

    def __str__(self):
        return self.title

# models.py

class LoginPage(models.Model):
    title = models.CharField(max_length=100, default="Login")
    image = models.ImageField(upload_to="login/", blank=True, null=True)

    class Meta:
        verbose_name = "Login Page"
        verbose_name_plural = "Login Page"

    def __str__(self):
        return self.title




#dashboard



class DashboardUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_image = models.ImageField(upload_to="dashboard/users/")
    logo = models.ImageField(upload_to="dashboard/logo/", blank=True, null=True)  # <--- NEW

    def __str__(self):
        return self.name



class DashboardStat(models.Model):
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    change = models.CharField(max_length=50, blank=True, null=True)
    change_type = models.CharField(
        max_length=10,
        choices=(("success", "Success"), ("danger", "Danger"), ("info", "Info")),
        blank=True,
        null=True,
    )
    note = models.CharField(max_length=100, blank=True, null=True)
    icon = models.ImageField(upload_to="dashboard/icons/")

    def __str__(self):
        return self.title



