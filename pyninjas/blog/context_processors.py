from .models import Tag


def tags(request):
    """
    Context processor that provides list of tags.
    :return: list of tags
    """
    _tags = Tag.objects.all()
    return {'tags': _tags}
