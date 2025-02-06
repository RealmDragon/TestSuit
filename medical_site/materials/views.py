from django.shortcuts import render, get_object_or_404, redirect
from medical_site.materials.models import Material


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
        form = Material(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materials:material_list') # перенаправляет на список материалов
    else:
        form = Material()
    return render(request, 'main/templates/add_doctor.html', {'doctor': form, 'title': 'Создание материала'})

def material_update(request, pk):
    """Обновляет существующий материал."""
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = Material(request.POST, instance=material)
        if form.is_valid():
            form.save()
            return redirect('materials:material_detail', pk=material.pk)
    else:
        form = Material(instance=material)
    return render(request, 'main/templates/edit_doctor.html', {'doctor': form, 'title': 'Редактирование материала'})


def material_delete(request, pk):
    """Удаляет материал."""
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('materials:material_list')
    return render(request, 'main/templates/delete_doctor.html', {'material': material})