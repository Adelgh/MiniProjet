from django.views import generic
from .models import Boutique, Produit
from .forms import BoutiqueForm, UserForm, ProduitForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def group_based_upload_to(instance, filename):
    return "image/boutique/{}/{}".format(instance.boutique.name, filename)

def detail(request, boutique_id):
    if not request.user.is_authenticated():
        return render(request, 'produit/login.html')
    else:
        user = request.user
        boutique = get_object_or_404(Boutique, pk=boutique_id)
        return render(request, 'produit/detail.html', {'boutique': boutique, 'user': user})

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'produit/login.html')
    else:
        boutiques = Boutique.objects.filter(user=request.user)
        produit_results = Produit.objects.all()
        query = request.GET.get("q")
        if query:
            boutiques = boutiques.filter(
                Q(name__icontains=query)


            ).distinct()
            produit_results = produit_results.filter(
                Q(title__icontains=query),
                Q(categorie__icontains=query)

            ).distinct()
            return render(request, 'produit/index.html', {
                'boutiques': boutiques,
                'produits': produit_results,
            })
        else:
            return render(request, 'produit/index.html', {'boutiques': boutiques})


def create_boutique(request):
    if not request.user.is_authenticated():
        return render(request, 'produit/login.html')
    else:
        form = BoutiqueForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            boutique = form.save(commit=False)
            boutique.user = request.user
            boutique.logo = request.FILES['logo']
            file_type = boutique.logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'boutique': boutique,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'produit/create_boutique.html', context)
            boutique.save()
            return render(request, 'produit/detail.html', {'boutique': boutique})
        context = {
            "form": form,
        }
        return render(request, 'produit/create_boutique.html', context)

def Activer(request, produit_id):
    produit = Produit.objects.get(pk=produit_id)
    produit.etat = "active"
    produit.save()
    return JsonResponse({'success':True})

def DesActiver(request, produit_id):
    produit = Produit.objects.get(pk=produit_id)
    produit.etat = "desactive"
    produit.save()
    return JsonResponse({'failure':True})


def delete_boutique(request, boutique_id):
    boutique = Boutique.objects.get(pk=boutique_id)
    boutique.delete()
    boutiques = Boutique.objects.filter(user=request.user)
    return render(request, 'produit/index.html', {'boutique': boutiques})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'produit/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Boutique.objects.filter(user=request.user)
                return render(request, 'produit/index.html', {'albums': albums})
            else:
                return render(request, 'produit/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'produit/login.html', {'error_message': 'Invalid login'})
    return render(request, 'produit/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                boutiques = Boutique.objects.filter(user=request.user)
                return render(request, 'produit/index.html', {'boutique': boutiques})
    context = {
        "form": form,
    }
    return render(request, 'produit/register.html', context)


def produits(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'produit/login.html')
    else:
        try:
            produit_ids = []
            for boutique in Boutique.objects.filter(user=request.user):
                for produit in boutique.produit_set.all():
                    produit_ids.append(produit.pk)
            users_produits = Produit.objects.filter(pk__in=produit_ids)
            if filter_by == 'favorites':
                users_produits = users_produits.filter(is_favorite=True)
        except Boutique.DoesNotExist:
            users_produits = []
        return render(request, 'produit/produits.html', {
            'produit_list': users_produits,
            'filter_by': filter_by,

        })




def create_produit(request, boutique_id):
    form = ProduitForm(request.POST or None, request.FILES or None)
    boutique = get_object_or_404(Boutique, pk=boutique_id)
    if form.is_valid():
        boutiques_produits = boutique.produit_set.all()
        for s in boutiques_produits:
            if s.title == form.cleaned_data.get("title"):
                context = {
                    'boutique': boutique,
                    'form': form,
                    'error_message': 'You already added that produit',
                }
                return render(request, 'produit/create_produit.html', context)
        produit = form.save(commit=False)
        produit.boutique = boutique

        produit.save()
        return render(request, 'produit/detail.html', {'boutique': boutique})
    context = {
        'boutique': boutique,
        'form': form,
    }
    return render(request, 'produit/create_produit.html', context)

def delete_produit(request, boutique_id, produit_id):
    boutique = get_object_or_404(Boutique, pk=boutique_id)
    produit = Produit.objects.get(pk=produit_id)
    produit.delete()
    return render(request, 'produit/detail.html', {'boutique': boutique})




class DetailView(generic.DetailView):
    model = Produit
    template_name = 'produit/detail-produit.html'

def post_list(request):
    list_produit = Produit.objects.all()
    paginator = Paginator(list_produit,4)
    page = request.GET.get('page')
    try:
        produits= paginator.page(page)
    except PageNotAnInteger:
        produits = paginator.page(1)
    except EmptyPage:
        produits = paginator.page(paginator.num_pages)
    return render(request, 'produit/produits.html',{'page':page, 'produits':produits})


def Categorie(request):
    produit_results = Produit.objects.all()
    categorie = Produit.choix_categorie
    if categorie:
        produit_results = produit_results.filter(
        Q(title__icontains=categorie)
         ).distinct()
    return render(request, 'produit/produits.html', {
        'produit1': produit_results,
    })

def favorite(request, produit_id):
    variable = get_object_or_404(Produit, pk=produit_id)
    try:
        if variable.is_favorite:
            variable.is_favorite = False
        else:
            variable.is_favorite = True
            variable.save()
    except (KeyError, Produit.DoesNotExist):
        return JsonResponse({'success':False})
    else:
        return JsonResponse({'success':True})



def smile(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    try:
        if produit.is_smile:
            produit.is_smile = False
        else:
            produit.is_smile = True
            produit.save()
    except (KeyError, Produit.DoesNotExist):
        return JsonResponse({'success':False})
    else:
        return JsonResponse({'success':True})






