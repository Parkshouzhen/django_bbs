from django import template

register = template.Library()

@register.filter # 템플릿 필터 만듦
def sub(value, arg): 
    return value - arg