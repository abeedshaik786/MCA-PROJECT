from django.apps import AppConfig


class JobkarleappConfig(AppConfig):
    name = 'jobkarleapp'
    
    def ready(self):
        import planety.signals
