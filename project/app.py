import json

import rhubarb
from django.conf import settings
from django.core.mail import send_mail
from jsonschema import validate
from rhubarb import registered_tasks

from core.storage import DatabaseStorage
from core.tasks import *


class App(rhubarb.AbstractApp):
    task_queue = DatabaseStorage()
    current = None

    def handle_result(self, result):
        if self.current and result:
            self.current.result = result
            self.current.is_done = True
            self.current.save()

    def perform_task(self):
        db_task = self.task_queue.get()
        if db_task:
            self.current = db_task
            task_name = db_task.name
            params = json.loads(db_task.params)
            task = registered_tasks.get(task_name)
            if task:
                print(f'{task_name}:\tпринято в обработку.')
                result = task(**params)
                send_mail(f'{task_name} id={db_task.id}', f'{result}', settings.SENDER_EMAIL, [db_task.email])
                return result
            else:
                print(f'{task_name}:\tзадача не существует.')

    def queue_task(self, task_name, params, email):
        task = registered_tasks.get(task_name)
        if task:
            validate(params, task.json_schema)
            self.task_queue.put(task_name, params, email)


app = App()
