from .views import Tag
from django.db.models import Count

# Django context processors available globally to templates
# https://stackoverflow.com/questions/2223429/django-global-template-variables
# https://dev.to/sarahhudaib/context-processors-in-django-15h2
# def common_tags(request):
def common_tags(request):
    common_tags = Tag.objects.annotate(num_posts=Count('taggit_taggeditem_items')).order_by('-num_posts')[:5]
    return {'common_tags': common_tags}
