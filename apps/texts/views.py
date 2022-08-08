from .models import Text
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
 
 
def generate_text_qr_code(request):
    if request.user.is_anonymous:
        return redirect("generate_code")
    template_name = "texts/text_view.html"
    if request.method == "POST":
         name = request.POST.get("text_name")
         description = request.POST.get("description")
         text = Text.objects.create(
             name=name, description=description, created_by=request.user
         )
         if text is not None:
             text.save()
             context = {"text": text}
             messages.success(request, f"qr code generated")
             return render(request, template_name, context)
         return redirect("generate_code")
    return render(request, template_name)
 
 
def get_text_qr_code(request, id):
    template_name = "texts/qr_info"
    text_context = get_object_or_404(Text, id=id)
    context = {"texts": text_context}
    return render(request, template_name, context)