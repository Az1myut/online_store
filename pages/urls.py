from django.urls import path
<<<<<<< HEAD
from .views import(
    AllProductsView, 
    add_file,
    get_file,
    index_files
)

=======
from .views import AllProductsView, BbCodeCreateView
>>>>>>> b755f87e829ee1b394a3d1c7a5ae764b906e867e
app_name = 'pages'

urlpatterns = [
    path('all_products', AllProductsView.as_view(), name='all_products'),
<<<<<<< HEAD
    path('add_file',add_file,name ='add_file'),
    path('files/get/<path:filename>', get_file, name = 'get_file'),
    path('files/',index_files, name='index_files'),

=======
    path('bbcode_create', BbCodeCreateView.as_view(), name='bbcode_create')
>>>>>>> b755f87e829ee1b394a3d1c7a5ae764b906e867e
 ]