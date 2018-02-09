from django.urls import include, path

urlpatterns = [
    path('course/', include('courses.urls.apis')),
]
