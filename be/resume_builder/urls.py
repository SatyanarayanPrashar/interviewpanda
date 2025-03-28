from django.urls import path
from resume_builder.views import generate_resume

urlpatterns = [
    path("generate-resume/", generate_resume, name="generate_resume"),
]