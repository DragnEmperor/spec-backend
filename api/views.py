from datetime import datetime

from django.core import serializers
from django.http.response import HttpResponseBadRequest
from django.http.response import JsonResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.utils.timezone import make_aware
from django.views.generic import CreateView
from django.views.generic import TemplateView

from api import models
from api.forms import AlumniForm
from api.forms import GalleryForm
from api.forms import ProjectForm
from api.forms import TeamForm
from api.forms import WorkshopForm


def dump_data(request):
    all_objects = [
        *models.TeamModel.objects.all(),
        *models.Workshop.objects.all(),
        *models.Gallery.objects.all(),
        *models.Alumni.objects.all(),
        *models.Project.objects.all(),
    ]
    data = serializers.serialize("json", all_objects, indent=2)
    extension = ".json"
    filename = datetime.now().strftime("%Y%m%d-%H%M%S") + extension
    response = HttpResponse(data, content_type="application/json")
    response["Content-Disposition"] = "attachment; filename=" + filename
    return response


def GalleryFormView(request):
    context = {}
    if request.method == "POST":
        upload_files = request.FILES.getlist("image")
        for file in upload_files:
            formset = GalleryForm(request.POST, {"image": file})
            if formset.is_valid():
                formset.save()
                context["message"] = "Successful"

            else:
                return HttpResponseBadRequest(formset.errors)

    context["form"] = GalleryForm()
    return render(request, "gallery.html", context)


def WorkshopFormView(request):
    context = {}
    if request.method == "POST":
        form = WorkshopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context["message"] = "Successful"

        else:
            context["error"] = form.errors[next(iter(form.errors))]

    context["form"] = WorkshopForm()
    return render(request, "workshop.html", context)


class Home(TemplateView):
    template_name = "home.html"


def TeamFormView(request):
    context = {}
    if request.method == "POST":
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context["message"] = "Successful"

        else:
            context["error"] = form.errors[next(iter(form.errors))]

    context["form"] = TeamForm()
    return render(request, "team.html", context)


def AlumniormView(request):
    context = {}
    if request.method == "POST":
        form = AlumniForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context["message"] = "Successful"

        else:
            context["error"] = form.errors[next(iter(form.errors))]

    context["form"] = AlumniForm()
    return render(request, "alumni.html", context)


def ProjectFormView(request):
    context = {}
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context["message"] = "Successful"

        else:
            context["error"] = form.errors[next(iter(form.errors))]

    context["form"] = ProjectForm()
    return render(request, "project.html", context)


def TeamUpdateView(request, pk):
    try:
        obj = models.TeamModel.objects.all().order_by("pk")[pk]
        obj.update_team_image_url()
        return JsonResponse({"message": f"Updated"})
    except IndexError:
        return JsonResponse({"message": "Does not exist"})


def WorkshopUpdateView(request, pk):
    try:
        obj = models.Workshop.objects.all().order_by("pk")[pk]
        obj.update_workshop_cover_url()
        return JsonResponse({"message": "Updated"})
    except IndexError:
        return JsonResponse({"message": "Does not exist"})


def GalleryUpdateView(request, pk):
    try:
        obj = models.Gallery.objects.all().order_by("pk")[pk]
        obj.update_gallery_image_url()
        return JsonResponse({"message": "Updated"})
    except IndexError:
        return JsonResponse({"message": "Does not exist"})


def AlumniUpdateView(request, pk):
    try:
        obj = models.Alumni.objects.all().order_by("pk")[pk]
        obj.update_alumni_image_url()
        return JsonResponse({"message": "Updated"})
    except IndexError:
        return JsonResponse({"message": "Does not exist"})


def ProjectUpdateView(request, pk):
    try:
        obj = models.Project.objects.all().order_by("pk")[pk]
        obj.update_project_cover_url()
        return JsonResponse({"message": "Updated"})
    except IndexError:
        return JsonResponse({"message": "Does not exist"})
