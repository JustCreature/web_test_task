import os

from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        from api.services import jobs

        if os.environ.get('RUN_MAIN', None) != 'true':
            jobs.start()
