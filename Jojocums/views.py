from django.shortcuts import render, get_object_or_404, redirect
from .forms import JogoForm
from .models import Jogo
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    return render(request, "menuprincipal.html", context)


@login_required
def create_jogo(request):
    message = ""
    if request.method == "POST":
        form = JogoForm(request.POST)
        if form.is_valid():
            form.save()
            mensagem = "Jogo criado com sucesso!"
    else:
        form = JogoForm()
    context = {"form": form, "message": message}

    return render(request, "Jojocums/jogo.html", context)


@login_required
def edit_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    try:
        if request.method == "POST":
            form = JogoForm(request.POST, instance=jogo)
            if form.is_valid():
                form.save()
                message = "Editado com sucesso!"
                context = {
                    "form": form,
                    "message": message,
                }
                return redirect("jogo")
        else:
            form = JogoForm(instance=jogo)
            context = {
                "form": form,
                "action": "edit",
                "article_id": jogo_id,
            }
            return render(request, "Jojocums/jogo.html", context)
    except:
        # Aqui podem ser armazenadas em log informações relevantes
        context = {}
        return render(request, "Jojocums/index.html", context)


@login_required
def delete_jogo(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    try:
        jogo.delete()
        return redirect("jogo")
    except:
        # Mensagens de erro
        context = {}
        return render(request, "Jojocums/jogos.html", context)


def jogo_list(request):
    jogos = Jogo.objects.all()

    genero = request.GET.get("genero")
    if genero:
        jogos = jogos.filter(genero=genero)

    context = {"jogos": jogos}

    return render(request, "Jojocums/jogos.html", context)


def jogo_read(request, jogo_id):
    jogo = get_object_or_404(Jogo, pk=jogo_id)
    context = {"jogo": jogo}

    return render(request, "Jojocums/jogo.html", context)
