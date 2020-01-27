from django.apps import AppConfig


class TennisConfig(AppConfig):
    name = 'tennis'

    def ready(self):
        import tennis.signals