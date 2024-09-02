from django.template import Library

register = Library()

@register.simple_tag
def course_time(time_string):
    print(time_string)
    tm = str(time_string)
    timeParts = [ int(s) for s in tm.split(':')]
    if timeParts[0] == 0 and timeParts[1] == 0:
        return "0 ساعت"
    elif timeParts[0] == 0 and timeParts[1] != 0:
        return f"{timeParts[1]}دقیقه "
    elif timeParts[0] != 0:
        return f" دقیقه{timeParts[1]}ساعت و{timeParts[0]}"
