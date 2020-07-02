from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .models import Item
from .filters import ItemFilter
from .forms import ItemForm

class ItemFilterView(LoginRequiredMixin, FilterView):
    model = Item
    filterset_class = ItemFilter
    # デフォルトの並び順を新しい順とする
    queryset = Item.objects.all().order_by('-created_at')

    # クエリ未指定の時に全件検索を行うために以下のオプションを指定（django-filter2.0以降）
    strict = False

    # 1ページあたりの表示件数
    paginate_by = 10

    # 検索条件をセッションに保存する or 呼び出す
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


class ItemFilterView(LoginRequiredMixin, FilterView):
  model = Item
  filterset_class = ItemFilter

  queryset = Item.objects.all().order_by('-created_at')

  strict = False

  paginate_by = 10 

  def get(self,request,**kwargs):
      if request.GET
          request.session
      else:
          request.GET = request.GET.copy()
          if 'query'in request.session.keys:
              for key in request.session['query'].keys():
                  request.GET[key] = request.session['query']

      
      return super().get(request,**kwargs)

class ItemdatailView(LoginRequiredMixin,DatailView):
  model = Item
  form_class = ItemForm
  success_url = reverse_lazy('index')


class ItemDeleteView(LoginRequiredMixin,DeleteView):
  model = Item
  success_url = reverse_lazu('index')


