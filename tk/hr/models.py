from django.db import models
from django.urls import reverse


class Department(models.Model):
    """Отдел или подразделение предприятия"""

    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)

    # Необязательное поле
    website = models.URLField(max_length=200, blank=True)

    def get_absolute_url(self):
        """ Ссылка на страницу представления самого объекта"""
        return reverse('hr:department-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Staff(models.Model):
    """Сотрудник подразделения"""

    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    bdate = models.DateField()

    # Необязательное поле
    email = models.EmailField(blank=True)

    photo = models.ImageField()
    department = models.ForeignKey(
        Department, null=True, on_delete=models.SET_NULL)
    # Можно было  on_delete = models.CASCADE, но удалять информацию просто так
    # не стоит, поставить какое-то значение по умолчанию для нераспределенных

    def get_absolute_url(self):
        """ Ссылка на страницу представления самого объекта"""
        return reverse('hr:staff-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "{0} {1}, {2}".format(self.fname, self.lname, self.department)
