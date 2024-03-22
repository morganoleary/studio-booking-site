from django.apps import AppConfig


class MemberConfig(AppConfig):
    """
    AppConfig class for the Member app.
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'member'

    def ready(self):
        import member.signals
