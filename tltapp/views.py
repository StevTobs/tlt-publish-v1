from django.shortcuts import render

# Create your views here.
def forminput(request):
    if request.method == "POST":
        namecus = request.POST.get("namecus")
        typebis = request.POST.get("selection")
        seminar_room = request.POST.get("seminar_room")
        if namecus == "":
            print("ใส่ข้อมูล")
        else:
            print(namecus)
            print(typebis)
            print(seminar_room)
    return render(request,"forminput.html")