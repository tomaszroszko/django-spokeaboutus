def get_source(slug):
    """
        return source class from given slug
    """
    from .models import SOURCES
    for cls in SOURCES:
        if cls.slug == slug:
            return cls