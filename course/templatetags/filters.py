
from textwrap import wrap
from django.template import Library
from course.models import Category, Course

register = Library()

@register.simple_tag
def course_time(time_string):
    print(time_string)
    tm = str(time_string)
    timeParts = [ int(s) for s in tm.split(':')]
    if timeParts[0] == 0 and timeParts[1] == 0:
        return "0 ساعت"
    elif timeParts[0] == 0 and timeParts[1] != 0:
        return f"{timeParts[1]} دقیقه"
    elif timeParts[0] != 0:
        return f" دقیقه{timeParts[1]}ساعت و{timeParts[0]}"


@register.filter
def same_course(category,course):
    same_courses = Course.objects.filter(category=category)
    result = same_courses.exclude(title=course)
    return result


@register.filter
def price_filter(price):
    if price != 0:
        price_str = str(price)[::-1]
        list_number = wrap(price_str, 3)
        sort_number = []
        for item in list_number:
            item = item[::-1]
            sort_number.append(item)
        sort_number.reverse()
        result = ",".join(sort_number)
        return f"{result} تومان"
    else:
        return "رایگان"


@register.filter
def range_number(number):
    range_list = []
    for i in range(number):
        range_list.append(i)
    return range_list