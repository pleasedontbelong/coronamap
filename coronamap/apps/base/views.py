from django.views.generic import ListView
from django.views.generic.base import TemplateView
from base.models import Entry
from django.http import JsonResponse
from django.db.models import Max, Min


class JSONResponseMixin:
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            safe=False,
            **response_kwargs
        )

    def get_data(self, context):
        return context


class HomepageView(TemplateView):
    template_name = "homepage.jinja2"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = Entry.objects.aggregate(
            Max('date_reported'), Min('date_reported')
        )
        context['min_date'] = data['date_reported__min'].strftime("%Y-%m-%d")
        context['max_date'] = data['date_reported__max'].strftime("%Y-%m-%d")
        return context


class NewCasesView(JSONResponseMixin, ListView):
    model = Entry

    def render_to_response(self, context, **response_kwargs):
        return self.render_to_json_response(context, **response_kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(
            date_reported=self.kwargs['date']
        ).values_list(
            'country_code', self.kwargs['field']
        )
        return qs

    def get_data(self, context):
        items = list(context['object_list'])
        items.insert(0, ("Country", self.kwargs['field']))
        return items
