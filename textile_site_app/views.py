from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from textile_site_app.forms import ItemCreateForm
from textile_site_app.models import Category, Item

def textile(request):
    categories = Category.objects.all()
    item = Item.objects.all()

    paginator = Paginator(item, 4)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'textile_site_app/items.html', {
        'categories': categories,
        'page_obj': page_obj,   
    })

def create_item(request):
    if request.method == "POST":
        form = ItemCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("items")
    else:
        form = ItemCreateForm()
    return render(request, "textile_site_app/item_create.html", {"form":form})

#@user_passes_test(isAdmin)
def delete_item(request, id):
    item_delete = get_object_or_404(Item, pk=id)
    if request.method=="POST":
        item_delete.delete()
        return redirect("items")
    else:
         return render(request, "textile_site_app/item_delete.html", {"item":item_delete})
    
def search(request):
    if "q" in request.GET and request.GET["q"] != " ":
        q = request.GET["q"]
        q_item = Item.objects.filter(title__contains=q).order_by("date")
    else:
        return redirect("items")

    return render(request, 'textile_site_app/search.html', {
        'items': q_item,
    })
