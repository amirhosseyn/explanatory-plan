from django.views.generic import TemplateView,CreateView
from django.urls import reverse_lazy
from .models import Plan
from .form import PlanForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'plan/index.html'


class PlanCreateView(CreateView):
    model = Plan
    form_class = PlanForm
    template_name = "plan/plan_create.html"
    success_url = reverse_lazy("plan:index")

    def get_form(self, form_class=None):
        form = super().get_form(PlanForm)
        # Customize the form layout based on fieldsets
        form.fieldsets = Plan.fieldsets
        return form


