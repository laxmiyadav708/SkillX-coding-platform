from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    home, dashboard, signup, login, logout,
    run_code, submit_code, get_hint,
    get_companies, get_company_questions,
    google_auth, resume_upload,
)
from .admin_views import (
    admin_list_users,
    admin_user_detail,
    admin_delete_user,
    admin_set_manager_role,
    admin_all_progress,
    admin_reset_progress,
)

urlpatterns = [
    # Public
    path("home/",           home),
    path("signup/",         signup),
    path("login/",          login),
    path("auth/google/",    google_auth),           # Google OAuth
    path("token/refresh/",  TokenRefreshView.as_view()),

    # User (authenticated)
    path("dashboard/",      dashboard),
    path("code/run/",       run_code),
    path("code/submit/",    submit_code),
    path("code/hint/",      get_hint),              # AI hint endpoint
    path("resume/upload/",  resume_upload),          # Resume interview
    path("logout/",         logout),

    # Companies
    path("companies/",                      get_companies),
    path("companies/<str:company_name>/",   get_company_questions),

    # Admin — FIX: use <str:username> to match admin_views signatures
    path("admin/users/",                            admin_list_users),
    path("admin/users/<str:username>/",             admin_user_detail),
    path("admin/users/<str:username>/delete/",      admin_delete_user),
    path("admin/users/<str:username>/role/",        admin_set_manager_role),
    path("admin/progress/",                         admin_all_progress),
    path("admin/progress/<str:username>/reset/",    admin_reset_progress),
]