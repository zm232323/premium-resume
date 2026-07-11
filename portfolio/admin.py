from django.contrib import admin
from .models import Contact, Project, Skill, Resume


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "subject",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    list_filter = (
        "created_at",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "featured",
        "created_at",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_filter = (
        "featured",
        "created_at",
    )

    search_fields = (
        "title",
        "technologies",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "active",
        "uploaded_at",
    )

    list_filter = (
        "active",
    )    