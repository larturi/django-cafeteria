from .models import Link


def ctx_dict(request):
    ctx = {}
    socials = []
    links = Link.objects.all()

    for link in links:
        socials.append({
            'key': link.key,
            'name': link.name,
            'url': link.url,
        })

    ctx['socials'] = socials

    return ctx
