import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import BaseFormView

from core.forms import TaskForm, EmailTaskForm
import core.tasks
from project.app import app


@method_decorator(csrf_exempt, name='dispatch')
class APIView(BaseFormView):
    http_method_names = ['post']
    form_class = TaskForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        data = json.loads(self.request.body.decode())
        processed = {
            'name': data.get('name', ''),
            'params': json.dumps(data.get('params', {})),
            'email': data.get('email', '')
        }
        kwargs.update(data=processed)
        return kwargs

    def form_valid(self, form):
        return JsonResponse({}, status=200)

    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors}, status=400)


class SyncTaskView(APIView):
    def form_valid(self, form):
        result = form.task(**form.params)
        return JsonResponse({'result': result})


class AsyncTaskView(APIView):
    form_class = EmailTaskForm

    def form_valid(self, form):
        app.queue_task(form.cleaned_data.get('name'), form.params, form.cleaned_data.get('email'))
        return JsonResponse({'status': 'OK'})

