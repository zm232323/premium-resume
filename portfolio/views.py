from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import ContactForm
from .models import Project, Skill, Resume


def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    resume = Resume.objects.filter(active=True).first()

    context = {
        "projects": projects,
        "skills": skills,
        "resume": resume,
        "project_count": projects.count(),
        "skill_count": skills.count(),
    }

    return render(request, "home.html", context)


def projects(request):
    projects = Project.objects.all()

    return render(
        request,
        "projects.html",
        {
            "projects": projects,
        },
    )


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "✅ Thank you! Your message has been sent successfully."
            )

            return redirect("contact")

    else:
        form = ContactForm()

    return render(
        request,
        "contact.html",
        {
            "form": form,
        },
    )


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    return render(
        request,
        "project_detail.html",
        {
            "project": project,
        },
    )