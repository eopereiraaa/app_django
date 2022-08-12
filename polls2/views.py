from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello World")


def test(request):
    return HttpResponse("Testando view test")


def test_html(request):
    name = 'criar um index.html dentro de um projeto Django'
    colors = [
        "yellow",
        "red",
        "blue",
        "pink",
    ]
    return render(request=request, template_name='index.html', context={'name': name, 'colors': colors})


# render é um shortcut
from django.template import loader
from .forms import LoginForm


# 1 View.
# DIY: Don't Repeat Yourself
def test_html_two(request):
    name = 'criar um index.html dentro de um projeto Django'
    colors = [
        "yellow",
        "red",
        "blue",
        "pink",
    ]
    form = LoginForm()
    response = loader.render_to_string(
        template_name='index.html',
        context={'name': name, 'colors': colors, 'form': form},
        request=request,
    )
    return HttpResponse(response)


# 1. View
# 1. Importamos ele
from .forms import Conversor, CategoryForm


def conversor(request):
    # Preciso criar uma instancia do formulario
    # Como acessar as informacoes do formulario enviadas na request.
    if request.method == 'POST':
        form = Conversor(request.POST)
        if form.is_valid():
            print("OS DADOS SAO VALIDOS!!!")
    else:
        form = Conversor()
    print("ENTROU AQUI NA VIEW!!!")
    return render(
        request=request,
        template_name='polls2/conversor.html',
        context={
            'form': form,
        }
    )


from django.views import View


class FirstCBView(View):
    template = 'polls2/conversor.html'

    def __render(self, context, request):
        return render(request=request,
                      template_name=self.template,
                      context=context
                      )

    def post(self, request):
        form = Conversor(request.POST)
        if form.is_valid():
            print("OS DADOS SÃO VÁLIDOS!!!")
            return self.__render(request=request,
                                 context={'form': form}
                                 )

    def get(self, request):
        print("[CLASS] ENTROU AQUI NA VIEW!!")
        form = Conversor()
        return self.__render(request=request,
                             context={'form': form}
                             )


class SecondConversor(FirstCBView):
    template = 'polls2/conversor_2.html'