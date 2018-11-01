from django.contrib import admin
from django.urls import path

from core.views import SyncTaskView, AsyncTaskView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sync/', SyncTaskView.as_view(), name='api_sync'),
    path('api/queue/', AsyncTaskView.as_view(), name='api_queue'),
]
