from django.shortcuts import render

# Create your views here.
def prodi1(request):
    judul = ["1. Program Studi Agribisnis", "2. Program Studi Agroekoteknologi", "3. Program Studi Ilmu Perikanan", "4. Program Studi Teknologi Pangan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfaperta.html', konteks)