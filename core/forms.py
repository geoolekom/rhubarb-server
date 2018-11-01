import json

from django import forms
from jsonschema import validate
from rhubarb import registered_tasks

from core.models import RhubarbTask


class TaskForm(forms.ModelForm):
    class Meta:
        model = RhubarbTask
        fields = 'name', 'params'

    task = None
    params = None

    def clean(self):
        super().clean()
        name = self.cleaned_data.get('name', '')
        params = self.cleaned_data.get('params', '{}')
        if name in registered_tasks:
            self.task = registered_tasks.get(name)
            try:
                self.params = json.loads(params)
            except Exception as e:
                self.add_error('params', str(e))
            else:
                try:
                    validate(self.params, self.task.json_schema)
                except Exception as e:
                    self.add_error('params', str(e))
        elif name:
            self.add_error('name', 'Такой задачи не существует.')


class EmailTaskForm(TaskForm):
    email = forms.EmailField()
