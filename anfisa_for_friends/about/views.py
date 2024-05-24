from typing import Any

from contest.models import Contest
from django.views.generic import TemplateView


class Description(TemplateView):
    template_name = 'about/description.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['total_count'] = Contest.objects.count()
        return context
