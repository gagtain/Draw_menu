from django import template

from ..models import *

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = list(MenuItem.objects.all().select_related('parent_menu', 'parent').filter(
        parent_menu__name=menu_name).order_by('parent_id').values())
    if not len(menu):
        return {'menu_name': menu_name}
    dicts = {menu_name:[]}
    for item in menu:
        if item['parent_id'] is None:

            dicts[menu_name].append(item)
    l = 0
    for i, obj in enumerate(dicts[menu_name]):
        try:
            if obj['name']==context['request'].path[1:-1].split('/')[1]:
                l = i
        except:
            pass
    url = context['request'].path[1:-1].split('/')
    reg_child(menu=menu, dicts=dicts[menu_name][l], urls=url)
    return {'menu':menu, 'dict':dicts[menu_name], 'menu_name': menu_name, 'url_parent_menu':url[0]}


def reg_child(menu, urls, dicts, k=1):
    menu = [x for x in menu if x != dicts]
    list_dick = [dicts]
    n = 0
    for i, obj in enumerate(list_dick):
        dicts['child'] = []
        for j, obj_menu in enumerate(menu):
            if obj['id'] == obj_menu['parent_id'] and obj['scr'] == "/".join(urls[0:k+1]):
                dicts['child'].append(obj_menu)
                dicts['child'][-1]['child']=[]
                n = i
    p = -1
    for i, obj in enumerate(list_dick[n]['child']):
        if obj['scr'] == "/".join(urls[0:k+2]):
            p = i
    k+=1
    if not (k==len(urls) or list_dick[n]['child'] == [] or p==-1):
        child = reg_child(menu=menu, dicts=list_dick[n]['child'][p], k=k, urls=urls)
        if child:
            return list_dick[n]['child'].append(child)
        else:
            return None
    else:
        return None



@register.inclusion_tag('child.html', takes_context=True)
def reg_child_template(context, dicts):
    return {'dict':dicts}