from django.contrib import admin
from django.urls import path, include
from app1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path("department/aplied_science", views.aplied_science, name="aplied_science"),
    path("gallery", views.gallery, name="gallery"),
    path("pages/<str:link>", views.pages, name="pages"),
    path("trainningap", views.trainningap, name="trainningap"),
    path("library", views.library, name="library"),
    path("workshop", views.workshop, name="workshop"),
    path("placement2021", views.placement2021, name="placement2021"),
    path("registration",views.registration, name="registration"),
    path("news/<str:link>", views.news, name="news"),
    path("mou/<str:link>", views.mou, name="mou"),
    path("mous",views.mous, name="mous"),


# abot
    path("aboutvdf", views.aboutvdf, name="aboutvdf"),
    path("our_inspiration", views.our_inspiration, name="our_inspiration"),
    path("pmassage", views.pmassage, name="pmassage"),
    path("primassage", views.primassage, name="primassage"),

    
    


# department

    path("about_as", views.about_as, name="about_as"),
    path("ce", views.ce, name="ce"),
    path("co", views.co, name="co"),
    path("el", views.el, name="el"),
    path("et", views.et, name="et"),
    path("me", views.me, name="me"),

# faculties

   
    path("facce", views.facce, name="facce"),
    path("facco", views.facco, name="facco"),
    path("facel", views.facel, name="facel"),
    path("facet", views.facet, name="facet"),
    path("facme", views.facme, name="facme"),
    path("facas", views.facas, name="facas"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 