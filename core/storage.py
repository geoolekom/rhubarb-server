import json
import rhubarb

from core.models import RhubarbTask


class DatabaseStorage(rhubarb.AbstractTaskQueue):
    lock = False

    def get(self):
        return RhubarbTask.objects.filter(is_done=False).first()

    def put(self, task_name, params, email):
        RhubarbTask.objects.create(name=task_name, params=json.dumps(params), email=email)
