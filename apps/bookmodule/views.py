from django.shortcuts import render

from .models import Book, Address ,Department, Student, Course,Student1
from django.db.models import Q,Count, Sum, Avg, Max, Min
from django.db import models



from django.http import HttpResponse
def index(request):
 name = request.GET.get("name") or "world!"
 return render(request, "bookmodule/index.html" , {"name": name}) 
def index2(request, val1 = 0): #add the view function (index2)
 return HttpResponse("value1 = "+str(val1))

def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)

def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')
def links(request):
 return render(request, 'bookmodule/links.html')
def format(request):
 return render(request, 'bookmodule/format.html')
def listing(request):
 return render(request, 'bookmodule/listing.html')
def tables(request):
 return render(request, 'bookmodule/table.html')
def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})

    return render(request, 'bookmodule/search.html')
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='i') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=Book.objects.filter(author__isnull =False).filter(title__icontains='i').filter(edition__gte = 1).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def lab8_task1(request):
    mybooks = Book.objects.filter(
        Q(author__isnull=False) & 
        Q(title__icontains='i') & 
        Q(edition__gte=1) & 
        Q(price__lte=80)
    )[:10]
    
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
def lab8_task2(request):
    
    edition_condition = Q(edition__gt=3)
    title_condition = Q(title__icontains='qu')
    author_condition = Q(author__icontains='qu')
    
    
    combined_condition = edition_condition & (title_condition | author_condition)
    
    
    books = Book.objects.filter(combined_condition)
    
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task3(request):
   
    edition_condition = ~Q(edition__gt=3) 
    title_condition = ~Q(title__icontains='qu')  
    author_condition = ~Q(author__icontains='qu')  
    

    combined_condition = edition_condition & (title_condition | author_condition)
    

    books = Book.objects.filter(combined_condition)
    
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task4(request):

    books = Book.objects.all().order_by('title')
    

    
    return render(request, 'bookmodule/bookList.html', {'books': books})

def lab8_task5(request):
    # Get all book statistics using aggregation
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    
    # Format the numbers for display
    stats_context = {
        'total_books': stats['total_books'],
        'total_price': f"{stats['total_price']:,.2f}",
        'avg_price': f"{stats['avg_price']:,.2f}",
        'max_price': f"{stats['max_price']:,.2f}",
        'min_price': f"{stats['min_price']:,.2f}",
    }
    
    return render(request, 'bookmodule/lab8_task5.html', stats_context)

def student_count_by_city(request):

    cities = Address.objects.annotate(
        student_count=models.Count('student')
    ).order_by('city')
    
    return render(request, 'bookmodule/student_count.html', {'cities': cities})


def department_student_counts(request):
    departments = Department.objects.annotate(
        student_count=Count('student1')
    ).order_by('name')
    
    return render(request, 'bookmodule/lab9task1.html', {
        'departments': departments
    })

def course_registration_counts(request):
    courses = Course.objects.annotate(
        student_count=Count('student1')
    ).order_by('title')
    
    return render(request, 'bookmodule/lab9task2.html', {
        'courses': courses
    })

def oldest_student_by_department(request):
    
    departments = Department.objects.all()
    department_data = []
    
    for dept in departments:
        oldest = Student1.objects.filter(department=dept).order_by('id').first()
        if oldest:
            department_data.append({
                'department': dept,
                'oldest_student': oldest
            })
    
    return render(request, 'bookmodule/lab9task3.html', {
        'department_data': department_data
    })

def departments_more_than_two_students(request):
    departments = Department.objects.annotate(
        student_count=Count('student1')
    ).filter(
        student_count__gt=2
    ).order_by(
        '-student_count'
    )
    
    return render(request, 'bookmodule/lab9task4.html', {
        'departments': departments
    })