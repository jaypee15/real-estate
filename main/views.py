from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

from main.models import State
from listings.models import Listing, ListingType
from accounts.models import Realtor


def bad_request(request, exception):
    return render(request, "main/errors/400.html", status=400)


def permission_denied(request, exception):
    return render(request, "main/errors/403.html", status=403)


def page_not_found(request, exception):
    return render(request, "main/errors/404.html", status=404)


def server_error(request):
    return render(request, "main/errors/500.html", status=500)


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["listings"] = Listing.objects.order_by("-created").filter(
            is_published=True
        )[:3]
        context["states"] = State.objects.all()
        context["list_types"] = ListingType.objects.all()
        context["index"] = True
        # SEO
        context["page_title"] = _("Realty Management." " Renting, buying and selling.")
        context["page_description"] = _(
            "Realty Management."
            "Services offered: renting, selling, buying and Consultation"
        )
        return context


class AboutView(TemplateView):
    template_name = "main/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["realtors"] = Realtor.objects.order_by("-hire_date")
        # Showcase Section Infos
        context["title"] = _("About us")
        context["subtitle"] = _("Real Estate and Consulting")
        # SEO
        context["page_title"] = _("About Us")
        context["page_description"] = _(
            "Realty Management."
            "Services include "
            "renting, selling, buying and consulting"
        )
        return context


class RobotsTXTView(TemplateView):
    template_name = "main/robots.txt"
