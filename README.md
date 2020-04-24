# Projeto de internacionalização

## Stack:
#### django(backend), jinja2(template)


Eu separei as strings do projeto em 3 categorias:
-   Backend strings (models, view...)
-   Template strings
-   JS strings

---

## Backend strings:

```python
from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    return render(request, 'index.html')
    string_from_view = _('Este texto foi criado na view')
    example = _('Texto da view')
    context = {'string_from_view': string_from_view,
               'example': example}
    return render(request, 'index.html', context=context)
```

---

## Template strings:
```html
 <h1 class="from-template">{{ _('Projeto de internacionalização') }}</h1>
```
Isso bastaria para funcionar com o django templates, mas o jinja precisa ser configurado.
Então nas configs do jinja:
```python
#jinja2.py
from django.templatetags.static import static
from django.urls import reverse
from django.utils import translation

from jinja2 import Environment


def environment(**options):
    env = Environment(extensions=['jinja2.ext.i18n', 'jinja2.ext.with_'], **options)
    env.install_gettext_translations(translation)
    env.globals.update({
        'static': static,
        'url': reverse,
    })
    return env
``` 

---

## JS strings:
O django provê um js para que o gettext funcione no js, então é preciso criar uma view para ele ter acesso:
```python
#urls.py
from django.views.i18n import JavaScriptCatalog


urlpatterns = [
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
```
O template precisa carregar esse javascript:

 #### **`django-template`**
```html
 <script type="text/javascript" src="{% url 'javascript-catalog' %}"></script>
```
 #### **`jinja2`**
```html
 <script type="text/javascript" src="{{ url('javascript-catalog') }}"></script>
```
 
 ---
 
 ## Como rodar:
 
 Backend strings e Template strings:
 ```
python manage.py makemessages
# vai gerar o django.po e lá será feita a tradução das strings do backend e do template
python manage.py compilemessages
# vai gerar o django.mo
```

 JS strings:
```
python manage.py makemessages -d djangojs
# vai gerar o djangojs.po e lá será feita a tradução das strings do js
python manage.py compilemessages
# vai gerar o djangojs.mo
``` 
