from django.shortcuts import render,redirect
from .import views
from crudapp.models import ProductDetails



def load_page(request):
    return render(request,"product.html")
def adddb(request):
    if request.method=='POST':
        pname=request.POST['product_name']
        des=request.POST['product_desc']
        qty=request.POST['product_quantity']
        price=request.POST['price']
        product= ProductDetails(product_name=pname,description=des,quantity=qty,price=price)
        product.save()
        return redirect('show_product_details')
    
def show_product_details(request):
    product=ProductDetails.objects.all() 
    return render(request,"show_product_details.html",{'prd':product}) 
def editpage(request,pk):
    prd=ProductDetails.objects.get(id=pk)
    return render(request,'edit.html',{'product':prd})
def edit_product_details(request,pk):
    if request.method=="POST":
        prd=ProductDetails.objects.get(id=pk)
        prd.product_name=request.POST.get('product_name')
        prd.description=request.POST.get('product_desc')
        prd.quantity=request.POST.get('product_quantity')
        prd.price=request.POST.get('price')
        prd.save()
        return redirect('show_product_details')
    return render(request,"edit.html")
def deletepage(request,pk):
    prd=ProductDetails.objects.get(id=pk)
    prd.delete()
    return redirect('show_product_details')
    





    

# Create your views here.
