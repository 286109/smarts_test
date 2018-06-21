from django.urls import path, reverse
from hr.views import (
    DepartmentDetail, DepartmentList, DepartmentCreate,
    DepartmentUpdate, DepartmentDelete, StaffList, StaffDetail, StaffCreate,
    StaffUpdate, StaffDelete
)

app_name = 'hr'
urlpatterns = [
    # Department model CRUD urls
    path('departments', DepartmentList.as_view(), name='department-list'),
    path(
        'department/<int:pk>', DepartmentDetail.as_view(),
        name='department-detail'
    ),
    path(
        'departments/create', DepartmentCreate.as_view(),
        name='department-create'
    ),
    path(
        'department/<int:pk>/update', DepartmentUpdate.as_view(),
        name='department-update'
    ),
    path(
        'department/<int:pk>/delete', DepartmentDelete.as_view(),
        name='department-delete'
    ),

    # Staff model CRUD urls
    path('staff', StaffList.as_view(), name='staff-list'),
    path(
        'staff/<int:pk>', StaffDetail.as_view(),
        name='staff-detail'
    ),
    path(
        'staff/create', StaffCreate.as_view(),
        name='staff-create'
    ),
    path(
        'staff/<int:pk>/update', StaffUpdate.as_view(),
        name='staff-update'
    ),
    path(
        'staff/<int:pk>/delete', StaffDelete.as_view(),
        name='staff-delete'
    ),


]