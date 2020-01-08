from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from blog.models import Post

# View referente à página principal do blog
def blog_index(request):
    posts = Post.objects.all().order_by('-created_at')
    all_tags = Post.tags.all()
    context = {
        "posts": posts,
        "all_tags": all_tags,
    }
    return render(request, "blog/blog_index.html", context)

# View para retornar a página individual de cada postagem
def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    all_tags = Post.tags.all()
    context = {
        "post": post,
        "all_tags": all_tags,
    }
    return render(request, "blog/blog_detail.html", context)

# View referente à página do autor
def blog_autor(request):
    return render(request, "blog/blog_autor.html")

# View para retornar os tutoriais do blog
def tutorial(request):
    tutorial_posts = Post.objects.filter(category__icontains='Tutorial')
    context = {'posts': tutorial_posts}
    return render(request, 'blog/blog_tutorial.html', context)


# View para retornar os artigos do blog
def article(request):
    article_posts = Post.objects.filter(category__icontains='Article')
    context = {'posts': article_posts}
    return render(request, 'blog/blog_article.html', context)

# View para renderizar a página para inscrição na lista de emails
def subscription(request):
    return render(request, "blog/subscription.html")

# View que recebe um item pesquisado e renderiza uma página como os posts correspondentes
def get_blog_queryset(request, query=None):
    posts = Post.objects.all().order_by('-created_at')
    all_tags = Post.tags.all()
    query = request.GET.get('search')
    item_pesquisado = str(request.GET.get('search'))
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts_filter = Post.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q) |
            Q(summary__icontains=q)
        ).distinct()
        for post in posts_filter:
            queryset.append(post)
    
    context = {
        "posts": posts,
        'queryset': queryset,
        'item_pesquisado': item_pesquisado,
        "all_tags": all_tags,
    }
    return render(request, 'blog/search_results.html', context)

# View que recebe um valor de tag e retorna um template com os posts correspondentes
def tagged(request):
    posts = Post.objects.all().order_by('-created_at') # Isso vai para a barra de arquivos
    all_tags = Post.tags.all()
    tag = request.GET.get('tag')
    # Filtrar a tag pelo nome
    posts_tags = Post.objects.filter(tags__name__in=[str(tag)])

    context = {
        'posts_tags': posts_tags,
        'tag': str(tag),
        "all_tags": all_tags,
        "posts": posts,
    }
    return render(request, 'blog/tags_results.html', context)