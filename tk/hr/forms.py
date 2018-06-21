from django.forms import ModelForm
from hr.models import Staff
from datetime import date
from django.core.exceptions import ValidationError


def calculate_age(born):
    today = date.today()
    return today.year - born.year - \
        ((today.month, today.day) < (born.month, born.day))


class StaffForm(ModelForm):
    """Класс для форм создания и измения объектов класса Staff."""

    class Meta:
        model = Staff
        fields = ['department', 'fname', 'lname', 'bdate', 'email', 'photo']

    def clean_bdate(self):
        """ Возраст должен быть от 18 лет"""

        required_age = 18
        bdate = self.cleaned_data['bdate']
        if calculate_age(bdate) < required_age:
            raise ValidationError('Too young...')
        return bdate
