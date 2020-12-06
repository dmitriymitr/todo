from django.template.defaulttags import register


@register.filter
def get_count(temp_list):
    temp = []
    if 6 - len(temp_list) > 0:
        for j in range(0, 6 - len(temp_list)):
            temp.append(j)
    return temp
