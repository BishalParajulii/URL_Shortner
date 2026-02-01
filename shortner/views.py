from django.shortcuts import render
from django.views.generic import TemplateView ,CreateView , ListView , UpdateView , DeleteView , View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ShortUrl
from .forms import ShortURLForm
from .utils import generate_short_code
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

class DashboardView(LoginRequiredMixin, View):
    template_name = 'shortner/dashboard.html'

    def get(self, request):
        urls = ShortUrl.objects.filter(user=request.user).order_by('-created_at')
        return render(request, self.template_name, {'urls': urls})

    def post(self, request):
        original_url = request.POST.get('original_url')

        if original_url:
            while True:
                code = generate_short_code()
                if not ShortUrl.objects.filter(short_code=code).exists():
                    break

            ShortUrl.objects.create(
                user=request.user,
                original_url=original_url,
                short_code=code
            )

        return redirect('dashboard')
    

        
class RedirectURLView(View):
    def get(self, request, code):
        url = ShortUrl.objects.filter(short_code=code).first()

        if not url or url.is_expired():
            return HttpResponse("This link has expired 😢", status=410)

        url.click_count += 1
        url.save(update_fields=['click_count'])

        return redirect(url.original_url)
    
    

    
    
class URLEditview(LoginRequiredMixin , UpdateView):
    model = ShortUrl
    fields = ["original_url"]
    template_name = 'shortner/edit_url.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return ShortUrl.objects.filter(user=self.request.user)
    
class URLDeleteView(LoginRequiredMixin , DeleteView):
    model = ShortUrl
    template_name = 'shortner/delete.html'
    success_url = reverse_lazy('dashboard')
    
    def get_queryset(self):
        return ShortUrl.objects.filter(user=self.request.user)