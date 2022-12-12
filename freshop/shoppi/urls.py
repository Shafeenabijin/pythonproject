from django.urls import path

from . import views
app_name='shoppi'
urlpatterns=[
    path('',views.fun,name='fun'),
    path('place/<int:place_id>',views.edit,name='edit'),
    path('add/',views.add_product,name='add_product'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]

