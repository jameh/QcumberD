from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from course_catalog.models import Course, Instructor
import re

def index(request):
    course_list = Course.objects.all().order_by('number')[:5]
    return render_to_response('course_catalog/index.html', {'course_list': course_list})

def course_detail(request, course_id=None, subject_abbr=None, course_number=None):
    c = None
    if course_id is not None:
        c = get_object_or_404(Course, pk=course_id)
    else:
        c = get_object_or_404(Course, subject__abbreviation=subject_abbr.upper(), number=course_number)
    return render_to_response('course_catalog/course_detail.html', {'course': c})


#For testing random things
def experiments(request):
    return render_to_response('course_catalog/experiments.html', {'insructor_list': []})
