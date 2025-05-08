from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
path('html5/links/', views.links, name="books.links"),
path('html5/text/formatting/', views.format, name="books.format"),
path('html5/listing/', views.listing, name="books.listing"),
path('html5/tables/', views.tables, name="books.tables"),
path('search/', views.search, name="books.search"),
path('search/', views.search, name="books.search"),
path('simple/query', views.simple_query, name="books.simple_query"),
path('complex/query', views.complex_query, name="books.complex_query"),
path('lab8/task1', views.lab8_task1, name="books.lab8_task1"),
path('lab8/task2', views.lab8_task2, name="books.lab8_task2"),
path('lab8/task3', views.lab8_task3, name="books.lab8_task3"),
path('lab8/task4', views.lab8_task4, name="books.lab8_task4"),
path('lab8/task5', views.lab8_task5, name="books.lab8_task5"),
path('lab8/task6', views.student_count_by_city, name="books.student_count_by_city"),
path('lab9/task1', views.department_student_counts, name="books.student_count_by_city"),
path('lab9/task2', views.course_registration_counts, name="books.student_count_by_city"),
path('lab9/task3', views.oldest_student_by_department, name="books.student_count_by_city"),
path('lab9/task4', views.departments_more_than_two_students, name="books.student_count_by_city"),
path('lab10_part1/listbooks', views.list_books10, name='list_books'),
path('lab10_part2/addbook', views.add_book, name='add_book'),
path('lab10_part3/editbook/<int:id>', views.edit_book, name='edit_book'),
path('lab10_part4/deletebook/<int:id>', views.delete_book, name='delete_book'),
path('lab10_part5/listbooks', views.list_books11, name='list1_books'),
path('lab10_part6/addbook', views.add_bookForms, name='add_book'),
path('lab10_part7/editbook/<int:id>', views.edit_bookForms, name='edit_book'),
path('lab10_part8/deletebook/<int:id>', views.delete_bookForms, name='delete_book'),
path('lab11_part1/liststudent', views.list_student1, name='list_student'),
path('lab11_part1/addstudent', views.add_student1, name='add_student1'),
path('lab11_part1/editstudent/<int:id>', views.edit_student1, name='edit_student1'),
path('lab11_part1/deletestudent/<int:id>', views.delete_student1, name='delete_student1'),

path('lab11_part2/liststudent', views.list_student2, name='list_student'),
path('lab11_part2/addstudent', views.add_student2, name='add_student1'),
path('lab11_part2/editstudent/<int:id>', views.edit_student2, name='edit_student1'),
path('lab11_part2/deletestudent/<int:id>', views.delete_student2, name='delete_student1'),
path('lab11_part3/listproduct', views.listProduct, name='delete_student1'),
path('lab11_part3/addproduct', views.addProduct, name='delete_student1'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)