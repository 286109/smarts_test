from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from hr.models import Staff, Department
from hr.forms import StaffForm

# Department model views


class DepartmentList(ListView):
    """Контроллер, представляющий список всех департаментов"""

    model = Department
    paginate_by = 20


class DepartmentDetail(DetailView):
    """Контроллер, представляющий детализированное представление информации об
    одном департаменте"""

    model = Department


class DepartmentCreate(CreateView):
    """Создание и сохранение в бд объекта класса Department"""

    model = Department
    fields = ['name', 'address', 'website']
    template_name_suffix = '_create_form'


class DepartmentUpdate(UpdateView):
    """Редактирование (обновление) и сохранение в бд объекта класса Department"""

    model = Department
    fields = ['name', 'address', 'website']
    template_name_suffix = '_update_form'


class DepartmentDelete(DeleteView):
    """Удаление из бд объекта класса Department"""

    model = Department
    success_url = reverse_lazy('hr:department-list')


# Staff model views part

class StaffList(ListView):
    """Контроллер, представляющий список всех служащих департаментов"""

    model = Staff
    paginate_by = 20


class StaffDetail(DetailView):
    """Контроллер, представляющий детализированное представление информации об
    одном служащем"""

    model = Staff


class StaffCreate(CreateView):
    """Создание и сохранение в бд объекта класса Staff"""

    model = Staff
    form_class = StaffForm
    template_name_suffix = '_create_form'


class StaffUpdate(UpdateView):
    """Редактирование (обновление) и сохранение в бд объекта класса Staff"""

    model = Staff
    form_class = StaffForm
    template_name_suffix = '_update_form'


class StaffDelete(DeleteView):
    """Удаление из бд объекта класса Staff"""

    model = Staff
    success_url = reverse_lazy('hr:staff-list')
