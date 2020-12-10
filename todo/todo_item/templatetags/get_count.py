from django.template.defaulttags import register
from todo.settings import DIV_COUNT

@register.filter
def get_count(temp_list):
    return range(DIV_COUNT - len(temp_list))
