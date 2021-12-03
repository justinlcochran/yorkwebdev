from django.shortcuts import render
from django.views import View


# Create your views here.
class UserDashboard(View):
    context = {}
    url_pattern = 'yorkdashboard/dashboard.html'

    def get(self, request):

        return render(request, self.url_pattern, self.context)