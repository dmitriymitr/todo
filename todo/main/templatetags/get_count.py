from django.template.defaulttags import register


@register.filter
def get_count():
    from main.views import data
    temp = []
    if 6 - len(data['lists']) > 0:
        for j in range(0, 6 - len(data['lists'])):
            temp.append(j)
    return temp
