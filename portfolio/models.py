from django.db import models
from django.utils.text import slugify


# ==========================
# Contact Model
# ==========================

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ==========================
# Project Model
# ==========================

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)

    short_description = models.TextField()
    full_description = models.TextField()

    technologies = models.CharField(
        max_length=300,
        help_text="Example: Django, Bootstrap, SQLite"
    )

    github_link = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)

    image = models.ImageField(upload_to="projects/")

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    @property
    def tech_list(self):
        return [
            tech.strip()
            for tech in self.technologies.split(",")
            if tech.strip()
        ]

    def __str__(self):
        return self.title


# ==========================
# Skill Model
# ==========================

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(
        max_length=100,
        default="bi bi-code-slash",
        help_text="Example: bi bi-filetype-html"
    )
    description = models.CharField(
        max_length=100,
        default="Technology"
    )
    percentage = models.PositiveIntegerField(default=80)

    def __str__(self):
        return self.name


# ==========================
# Resume Model
# ==========================
    
class Resume(models.Model):
    title = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to="resume/")
    active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.active:
            Resume.objects.filter(active=True).update(active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title