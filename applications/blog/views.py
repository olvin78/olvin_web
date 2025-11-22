from django.shortcuts import render

# Create your views here.

from .models import Post
from django.shortcuts import render
from django.db.models import Q
from .models import Post, Tag

from django.shortcuts import render, get_object_or_404





def index(request):
    query = request.GET.get('q', '').strip()
    tag_slug = request.GET.get('tag', '').strip()

    # Todas las etiquetas disponibles que tienen posts publicados
    all_tags = Tag.objects.filter(posts__is_published=True).distinct().order_by("name")

    # Base: posts publicados
    base_qs = Post.objects.filter(is_published=True).order_by('-published_at')

    active_tag = None
    if tag_slug:
        active_tag = Tag.objects.filter(slug=tag_slug).first()
        if active_tag:
            base_qs = base_qs.filter(tags__slug=tag_slug)

    # Última publicación (dentro del filtro si hay tag)
    latest_post = base_qs.first()

    # Resto de posts (para tarjetas de abajo)
    posts_qs = base_qs
    if latest_post:
        posts_qs = posts_qs.exclude(id=latest_post.id)

    # Filtro por texto si hay búsqueda
    if query:
        posts_qs = posts_qs.filter(
            Q(title__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(content__icontains=query)
        )

    recent_posts = posts_qs[:9]

    context = {
        "latest_post": latest_post,
        "recent_posts": recent_posts,
        "query": query,
        "results_count": posts_qs.count(),
        "all_tags": all_tags,
        "active_tag": active_tag,
    }
    return render(request, 'blog/index.html', context)




def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)

    # Posts relacionados por etiquetas
    related = Post.objects.filter(
        tags__in=post.tags.all()
    ).exclude(id=post.id).distinct()[:3]

    return render(request, "blog/detail.html", {
        "post": post,
        "related_posts": related,
    })