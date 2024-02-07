from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from connects.views import AdminContactView
from django.contrib.auth import views as auth_views


handler400 = "main.views.bad_request"
handler403 = "main.views.permission_denied"
handler404 = "main.views.page_not_found"
handler500 = "main.views.server_error"


urlpatterns = i18n_patterns(
    path("i18n/", include("django_translation_flags.urls")),
    path("admin/", admin.site.urls),
    path("admin/contact/", AdminContactView.as_view(), name="admin-contact"),
    path("", include("main.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/auth/password_reset_done.html"
        ),
        name="password-reset-done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(  # noqa
            template_name="accounts/auth/password_reset_confirm.html"
        ),
        name="password-reset-confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/auth/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("listings/", include("listings.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),
    path("contacts/", include("connects.urls")),
    path("listings/", include("files.urls")),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
