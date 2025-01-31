from django.shortcuts import render, get_object_or_404, redirect
from .models import Material
from .forms import MaterialForm # если у вас есть форма

def material_list(request):
    """Отображает список всех материалов."""
    materials = Material.objects.all()
    return render(request, 'materials/material_list.html', {'materials': materials})

def material_detail(request, pk):
    """Отображает подробную информацию о конкретном материале."""
    material = get_object_or_404(Material, pk=pk)
    return render(request, 'materials/material_detail.html', {'material': material})

def material_create(request):
    """Создает новый материал."""
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materials:material_list') # перенаправляет на список материалов
    else:
        form = MaterialForm()
    return render(request, 'materials/material_form.html', {'form': form, 'title': 'Создание материала'})

def material_update(request, pk):
    """Обновляет существующий материал."""
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('materials:material_detail', pk=material.pk)
    else:
        form = MaterialForm(instance=material)
    return render(request, 'materials/material_form.html', {'form': form, 'title': 'Редактирование материала'})


def material_delete(request, pk):
    """Удаляет материал."""
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('materials:material_list')
    return render(request, 'materials/material_confirm_delete.html', {'material': material})