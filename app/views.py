from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Producto
from .forms import ProductoForm


# ==========================
# 📋 Vista para listar productos
# ==========================
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'app/producto_list.html', {'productos': productos})


# ==========================
# 🔍 Vista para ver detalle de un producto
# ==========================
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'app/producto_detail.html', {'producto': producto})


# ==========================
# ➕ Vista para crear un nuevo producto
# ==========================
def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'app/producto_form.html', {'form': form})


# ==========================
# ✏️ Vista para actualizar un producto existente
# ==========================
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app/producto_form.html', {'form': form})


# ==========================
# 🗑️ Vista para eliminar un producto
# ==========================
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'app/producto_confirm_delete.html', {'producto': producto})


# ==========================
# 🧾 Nueva vista para generar PDF de productos
# ==========================
def producto_pdf(request):
    productos = Producto.objects.all()
    template = get_template('app/producto_pdf.html')  # Plantilla para el PDF
    html = template.render({'productos': productos})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="productos.pdf"'

    # Crear el PDF con xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Si hubo un error al generar el PDF, mostrarlo en texto
    if pisa_status.err:
        return HttpResponse('Ocurrió un error al generar el PDF <pre>' + html + '</pre>')
    
    return response