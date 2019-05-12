from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "queenwiki.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import queenwiki.users.signals  # noqa F401
        except ImportError:
            pass
