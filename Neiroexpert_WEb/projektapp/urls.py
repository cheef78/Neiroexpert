from django.urls import path
import projektapp.views as projektapp

app_name = 'projektapp'

urlpatterns = [
    path( '' , projektapp.projekt, name= 'view' ),
    path( 'create/' , projektapp.projekt_create, name= 'create' ),
    path( 'load/<int:pk>' , projektapp.projekt_load, name= 'load' ),
    # path('edit/<int:pk>/<int:quantity>/', projektapp.projekt_edit, name='edit')
]