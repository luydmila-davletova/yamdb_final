import datetime as dt

from django.core.exceptions import ValidationError


def validate_year(value):
    """Валидатор года для Модели Title."""
    current_year = dt.datetime.now().year
    if not 0 <= value <= current_year:
        raise ValidationError(
            'Укажите год создания не позже текущего!',
            params={'value': value},
        )
    return value
