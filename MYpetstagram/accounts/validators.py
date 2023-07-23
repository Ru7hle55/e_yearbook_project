from django.core.exceptions import ValidationError


def validate_only_alphabetical_letters(name):
    if not name.isalpha():
        raise ValidationError("The name should contain only alphabetical letters !")