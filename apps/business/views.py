from .models import Business
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect

def generate_text_qr_code(request):
    if request.user.is_anonymous:
        return redirect("generate_code")
    template_name = "texts/text_view.html"
    if request.method == "POST":
         name = request.POST.get("text_name")
         bussiness_name = request.POST.get("bussiness_name")
         email = request.POST.get('email')
         phone_no = request.POST.get('phone_number')
         location = request.POST.get("location")
         bio = request.POST.get('bio')
         logo = request.POST.get('logo')

         business = Business.objects.create(
             name=name, 
             bussiness_name=bussiness_name, 
             email= email, 
             phone_no = phone_no, 
             location = location,
             bio = bio,
         )
         if business is not None:
             business.save()
             context = {"business": business}
             messages.success(request, f"qr code generated")
             return render(request, template_name, context)
         return redirect("generate_code")
    return render(request, template_name)
 
 
def get_text_qr_code(request, id):
    template_name = "texts/qr_info"
    text_context = get_object_or_404(Text, id=id)
    context = {"texts": text_context}
    return render(request, template_name, context)