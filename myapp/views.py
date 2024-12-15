from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# View to display all items
from django.shortcuts import render


def item_list(request):
    items = Item.objects.all()  # Assuming you're fetching items from the database
    return render(request, 'myapp/item_list.html', {'items': items})

# View to create a new item


def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the item list page after saving
            return redirect('item_list')
    else:
        form = ItemForm()

    return render(request, 'myapp/create_item.html', {'form': form})

# View to update an existing item


# def update_item(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == 'POST':
#         form = ItemForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('item_list')
#     else:
#         form = ItemForm(instance=item)
#     return render(request, 'update_item.html', {'form': form})
def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            # Redirect to the item list page after saving
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)

    return render(request, 'myapp/update_item.html', {'form': form})

# View to delete an item


# def delete_item(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == 'POST':
#         item.delete()
#         return redirect('item_list')
#     return render(request, 'delete_item.html', {'item': item})


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        # Redirect to the item list page after deleting
        return redirect('item_list')
    return render(request, 'myapp/delete_item.html', {'item': item})

# List all items


# def item_list(request):
#     items = Item.objects.all()
#     return render(request, 'myapp/item_list.html', {'items': items})

# # Create a new item


# def item_create(request):
#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('item_list')
#     return render(request, 'myapp/item_form.html', {'form': ItemForm()})

# # Update an existing item


# def item_update(request, id):
#     item = Item.objects.get(id=id)
#     if request.method == 'POST':
#         form = ItemForm(request.POST, instance=item)
#         if form.is_valid():
#             form.save()
#             return redirect('item_list')
#     return render(request, 'myapp/item_form.html', {'form': ItemForm(instance=item)})

# # Delete an item


# def item_delete(request, id):
#     item = Item.objects.get(id=id)
#     item.delete()
#     return redirect('item_list')
