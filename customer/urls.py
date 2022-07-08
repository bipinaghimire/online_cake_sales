from customer import views
from django.urls import path

urlpatterns=[
    path("",views.index),
    path("create", views.create),
    path("save", views.saveFn),
    path("edit/<int:id>", views.edit, name='customer_edit'),
    path("update/<int:id>", views.update),
    path("delete/<int:id>", views.delete),
]