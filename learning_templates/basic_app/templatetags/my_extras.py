
# CREATING CUSTOM FILTERS!
# IN VIEWS.PY MAKE FOLLOWING CHANGES
# def index(request):
#     context_dict = {'text':'hello world','number':'100'}
#     return render(request,'basic_app/index.html',context_dict)
#there are 2 ways to register custom filters!

#1. register.filter('cut',cut) ---- > where 'cut' is the name for the filter and cut is the function!
# in index.html -----> {{text | cut:'hello'}}-----> this cuts hello from the text

# 2 . using DECORATORS
# @register.filter(name = 'cut')
# in index.html -----> {{text | cut:'hello'}}-----> this cuts hello from the text
# REFERNCES: https://docs.djangoproject.com/en/2.0/topics/templates/#filters
# --------------------------------------------------------------------------------------------------------

from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value,arg):
    '''this cuts out all vlues of arg from the string 'value'
    '''
    return value.replace(arg,'')

#register.filter('cut',cut)
