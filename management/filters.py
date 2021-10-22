from django.views.generic import ListView

from root.filters import BookFilter



class ListViewWithFilter(ListView):
    model = None
    target_filter = None
    filtered_items = None

    def get_queryset(self):
        queryset = self.model.objects.all()
        self.filtered_items = self.target_filter(self.request.GET, queryset = queryset)
        return self.filtered_items.qs
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filtered_items'] = self.filtered_items
        return context
    
