from .views import Tag

# Django context processors available globally to templates
# https://stackoverflow.com/questions/2223429/django-global-template-variables
# https://dev.to/sarahhudaib/context-processors-in-django-15h2
def common_tags(request):
    common_tags = Tag.objects.all()[:6]
    return {'common_tags': common_tags}