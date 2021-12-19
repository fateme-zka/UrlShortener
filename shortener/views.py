from django.views.generic import CreateView, DetailView
from .forms import UrlForm
from django.shortcuts import reverse
from .models import Url
import uuid


class CreateUrlView(CreateView):
    model = Url
    template_name = 'shortener/home_page.html'
    form_class = UrlForm

    def form_valid(self, form):
        url = form.save(commit=False)
        url.uuid = str(uuid.uuid4())[:5]
        url.save()
        return super().form_valid(form)

    # def get_success_url(self):
    #     pk = self.kwargs['pk']
    #     return reverse('result', args=[pk])

    def get_success_url(self):
        return reverse('result', args=(self.object.id,))


class DetailUrlView(DetailView):
    model = Url
    template_name = 'shortener/result.html'
    context_object_name = 'url'

# ----------------------------------------

# def create_url(request):
#     if request.method == "POST":
#         link = request.POST['link']
#         uid = str(uuid.uuid4())[:5]
#         new_url = Url(link=link, uuid=uid)
#         new_url.save()
#         # return render(request, 'shortener/result.html', {'uid': uid})
