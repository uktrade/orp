from django.apps import AppConfig


class SearchConfig(AppConfig):
    """
    Configuration class for the Find business regulations Search application.

    Attributes:
        name (str): The full Python path to the application.
        verbose_name (str): A human-readable name for the application.
        default_auto_field (str): Specifies the type of auto-created
                                  primary key field to use.

    """

    name = "orp_search"
    verbose_name = "Find business regulations application functionality"
    default_auto_field = "django.db.models.BigAutoField"
