from django.core.management import BaseCommand

from project.app import app


class Command(BaseCommand):
    help = 'Запускает очередь задач.'

    def handle(self, *args, **options):
        print('Очередь запущена.')
        app.run()
