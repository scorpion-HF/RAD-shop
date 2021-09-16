from django.views.generic import DetailView, ListView
from .models import Branch


class SelectBranch(ListView):
    model = Branch
    template_name = 'branches/select-branch.html'
    context_object_name = 'branches'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        return context


class BranchFirstPage(DetailView):
    model = Branch
    template_name = 'branches/first-page.html'
    context_object_name = 'branch'
    pk_url_kwarg = 'branch'
