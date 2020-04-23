from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    string_from_view = _('Este texto foi criado na view')
    example = _('Texto da view')
    context = {'string_from_view': string_from_view,
               'example': example}
    return render(request, 'index.html', context=context)
