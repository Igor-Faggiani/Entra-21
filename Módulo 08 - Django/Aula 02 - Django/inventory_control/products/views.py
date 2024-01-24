from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Product
from .forms import ProductForm

# Create your views here.


def index(request):
    products = Product.objects.order_by("-id")

    # Aplicando a paginação
    paginator = Paginator(products, 2)
    # /fornecedores?page=1 --> Obtendo a página da URL
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"products": page_obj}

    return render(request, 'products/index.html', context)


def search(request):
    # Obtendo o valor da requisição (Formulário)
    search_value = request.GET.get("q").strip()

    # Verificando se algo foi digitado
    if not search_value:
        return redirect("products:index")

    # Filtrando os fornecedores
    # "Q" é usado para combinar filtros ( & ou | )
    products = Product.objects \
        .filter(Q(fantasy_name__icontains=search_value) |
                Q(comany_name__icontains=search_value)) \
        .order_by("-id")

    # Criado o paginator
    paginator = Paginator(products, 100)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"products": page_obj}

    return render(request, "index.html", context)


def create(request):
    form_action = reverse("products:index")
    # POST
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            
            messages.success(request, "O fornecedor foi cadastrado com sucesso!") # Passando a mensagem no TOAST caso o cadastro for bem sucessido
            
            return redirect("products:index")
        
        messages.error(request, "Falha ao cadastrar o fornecedor. Verifique o preenchimento dos campos.") # Retorna erro caso o cadastro do fornecedor for mal sucedida
        
        print(form.errors)

        cotext = {"form": form}

        return render(request, "create.html", cotext)

    # GET
    form = ProductForm()

    context = { "form": form }

    return render(request, "create.html", context)


def update(request, slug):
    Product = get_object_or_404(Product, slug=slug)
    form_action = reverse("products:update", args=(Product.slug,)) # Obtendo a URL da rota de atualização
    
    # POST
    if request.method == "POST":
        form = ProductForm(request.POST, instance=Product)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Fornecedor atualizado com sucesso!")
            
            return redirect("products:index")
        
        context = {
            "form_action": form_action,
            "form": form,
        }
        
        return render(request, "create.html", context)
    
    # GET
    form = ProductForm(instance=Product)
    
    context = {
        "form_action": form_action,
        "form": form,
    }
    
    return render(request, "create.html", context)


@require_POST
def delete(request, id):
    Product = get_object_or_404(Product, pk=id)
    Product.delete()

    return redirect("products:index")


@require_POST
def toggle_enabled(request, id):
    Product = get_object_or_404(Product, pk=id)

    Product.enabled = not Product.enabled
    Product.save()

    return JsonResponse({"message": "success"})
