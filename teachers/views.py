from django.shortcuts import render
from teachers.models import MethodicalAssociation, Teacher

def methodical_work(request):
    methodical_associations = MethodicalAssociation.objects.all()

    return render(request, 'methodical-work/methodical-work.html', {'methodical_associations' : methodical_associations})

def mo(request, mo_id):
    methodical_association = MethodicalAssociation.objects.filter(id = mo_id)[0]
    mo_name = methodical_association.title
    teachers = Teacher.objects.filter(methodical_association__id = mo_id)

    return render(request, 'methodical-work/methodical-association.html', {"teachers" : teachers, "mo_name":mo_name})

def administration(request):
    dr = Teacher.objects.get(special_position = 'dr')
    dp = Teacher.objects.filter(special_position = 'dp')
    
    return render(request, 'methodical-work/administration.html', {'dr': dr, 'dp': dp})

def legal_framework(request):
    return render(request, 'methodical-work/legal-framework.html')

def guidelines(request):
    return render(request, 'methodical-work/guidelines.html')

def pedagogics_perspective_plan(request):
    page_name = 'Перспективний план атестації педагогів'
    links = (
        ['', 'https://drive.google.com/file/d/10rmLE8LF4VBDeNvZoup8Gi55bYuYYvJr/preview'],
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})

def pedagogical_certification(request):
    page_name = 'Перспективний план атестації педагогів'
    links = (
        ['Графік атестації педагогічних працівників Долинського наукового ліцею №1', 'https://drive.google.com/file/d/1HZ3VZHH7jz8fgmNZoTEYXSeAgG_JdkWT/preview'],
        ['Список педагогічних працівників Долинського наукового ліцею №1, які підлягають черговій атестації у 2019 році', 'https://drive.google.com/file/d/1GQD431of0bds0TQv1aaCpJlFj9eNxM5S/preview'],
        ['Протокол засідання атестаційної комісії І рівня Долинського наукового ліцею №1', 'https://drive.google.com/file/d/1kBFSRAVu2LV97NkZOUf6SMbGEMCKVitu/preview'],
    )
    return render(request, 'dnl1/google-documents-page.html', {'page_name': page_name, 'links': links})