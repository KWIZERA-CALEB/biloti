from django.shortcuts import render, redirect
from .models import ClassDetail, SchoolYear, SchoolTerm


# Create your views here.

def addClass(request):
    if request.method == "POST":
        class_name = request.POST.get('class_name')
        save_class = ClassDetail(
            class_name=class_name
        )

        try:
            save_class.save()
            return redirect('home')
        except:
            print('Failed to add class')
            return redirect()
    return render(request, 'headteacher/add-class.html')

def addSchoolYear(request):
    if request.method == "POST":
        year_name = request.POST.get('year_name')
        save_year = SchoolYear(
            year_name=year_name
        )

        try:
            save_year.save()
            return redirect('home')
        except:
            print('Failed to add class')
    # context = {}
    return render(request, 'headteacher/add-school-year.html')


def renderSchoolYear(request, pk):
    school_year = SchoolYear.objects.get(id=pk)
    if request.method == "POST":
        term_name = request.POST.get('term_name')
        try:
            run_add_term = SchoolTerm(term_name=term_name,term_year_link=school_year)
            run_add_term.save()
            return redirect('school-year', pk=school_year.id)
        except Exception as e:
            print(f'Failed to add Term: {e}')

    render_terms = SchoolTerm.objects.filter(term_year_link=school_year)

    term = SchoolTerm.objects.get(id=pk)

    context = {'school_year':school_year, 'term':term, 'render_terms':render_terms}
    return render(request, 'headteacher/school-year.html', context)


def renderTerm(request, pk):
    term = SchoolTerm.objects.get(id=pk)
    context = {'term':term}
    return render(request, 'headteacher/term.html', context)