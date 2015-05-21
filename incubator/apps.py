from django.apps import AppConfig

class IncubatorConfig(AppConfig):
    name = 'incubator'
    verbose_name = "incubator"

    def ready(self):
        # register the signals
        import incubator.signals 
