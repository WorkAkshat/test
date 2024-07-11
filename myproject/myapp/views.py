from django.shortcuts import render, redirect
from .forms import TreeForm

def upload_tree(request):
    if request.method == 'POST':
        form = TreeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TreeForm()
    return render(request, 'upload_tree.html', {'form': form})

def success(request):
    return render(request, 'success.html')
