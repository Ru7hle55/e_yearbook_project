from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'MYpetstagram.accounts'

    def ready(self):
        import MYpetstagram.accounts.signals
        result = super().ready()
        return result