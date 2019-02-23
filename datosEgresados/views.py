from django.shortcuts import render

# Create your views here.

'''def add_element(request,pk):
    service = get_object_or_404(Service, id=pk)
    
    if(service.theme=='catalog'):
        form = MissingItemForm()
        if request.method == 'POST':
            form = MissingItemForm(request.POST, request.FILES)

    elif(service.theme=='directory'):
        form = OfficeForm()
        if request.method == 'POST':
            form = OfficeForm(request.POST)

    elif(service.theme=='map'):
        form = LocationForm()
        if request.method == 'POST':
            form = LocationForm(request.POST)
    
    else:
        return redirect(reverse('service-configure', kwargs={'pk': service.id}))

    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.service = service
            post.save()
            return redirect(reverse('service-configure', kwargs={'pk': service.id}))
    return render(request, 'Services/'+str(service.theme)+'_form.html', {'form':form, 'service':service})'''