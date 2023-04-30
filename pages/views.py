<<<<<<< HEAD
import os
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from products.models import SingleProduct
from .forms import AddFileForm
from datetime import datetime
from pathlib import Path
from django.conf import settings
=======
from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView
from .models import BbCodeModel
from .forms import BbCodeForm
from products.models import SingleProduct

>>>>>>> b755f87e829ee1b394a3d1c7a5ae764b906e867e
from icecream import ic
# Create your views here.

class AllProductsView(TemplateView):
    template_name = 'pages/show_page/all_products.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = SingleProduct.objects.prefetch_related('images')
        return context

<<<<<<< HEAD
def add_file(request):
    if request.method == 'POST':
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            ic(uploaded_file)
            file_name = f"{datetime.now().timestamp()}{os.path.splitext(uploaded_file.name)[1]}"
            ic(file_name)
            file_with_path = Path(settings.FILES_ROOT, file_name)
            ic(file_with_path)
            with open(file_with_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            redirect ('pages:index_files')
    else:
        form = AddFileForm()
    context = {'form' : form}
    template_name = "pages/files/add_file.html"

    return render(request, template_name=template_name, context=context)

def get_file(request, filename):
    ic(filename)
    from django.http import FileResponse
    fn = Path(settings.FILES_ROOT, filename)
    ic(fn)
    return FileResponse(open(fn, 'rb'), content_type='application/ostet-stream')

def index_files(request):
    template_name = "pages/files/indexx.html"
    files = []
    for entry in os.scandir(settings.FILES_ROOT):
      
        files.append(os.path.basename(entry))

    if not files:
    
        no_files = 'Файлов нет'
        context = {'no_file' : no_files}
    else:
        context = {'files' : files}
    return render(request, template_name, context=context)
=======
class BbCodeCreateView(CreateView):
    model = BbCodeModel
    form_class = BbCodeForm
    template_name = 'pages/bbcode/bbcode_create.html'
    success_url = '/'
    # def get(self, request, *args, **kwargs):
    #     return reverse(request, self.template_name, context={})

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save(commit=True)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
>>>>>>> b755f87e829ee1b394a3d1c7a5ae764b906e867e
