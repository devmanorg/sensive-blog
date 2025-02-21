from django.shortcuts import render
from blog.models import Comment, Post, Tag
from django.db.models import Count, Prefetch


def serialize_post(post):
    return {
        'title': post.title,
        'teaser_text': post.text[:200],
        'author': post.author.username,
        'comments_amount': post.comments_count,
        'image_url': post.image.url if post.image else None,
        'published_at': post.published_at,
        'slug': post.slug,
        'tags': [serialize_tag(tag) for tag in post.tags.all()],
        'first_tag_title': post.tags.first().title if post.tags.exists() else None,
    }


def serialize_tag(tag):
    return {
        'title': tag.title,
        'posts_with_tag': getattr(tag, 'posts_count', 0),
    }


def index(request):
    most_popular_posts = (
        Post.objects
        .popular()
        .prefetch_related("tags", "author")
        .annotate(comments_count=Count('comments'))[:5]
    )

    fresh_posts = (
        Post.objects
        .annotate(comments_count=Count('comments'))
        .order_by('-published_at')
        .prefetch_related("tags", "author")[:5]
    )
    
    most_popular_tags = (
        Tag.objects
        .annotate(posts_count=Count('posts'))
        .order_by('-posts_count')[:5]
    )
    
    context = {
        'most_popular_posts': [serialize_post(post) for post in most_popular_posts],
        'page_posts': [serialize_post(post) for post in fresh_posts],
        'popular_tags': [serialize_tag(tag) for tag in most_popular_tags],
    }
    return render(request, 'index.html', context)


def post_detail(request, slug):
    post = (
        Post.objects
        .prefetch_related("author", "tags", "likes")
        .annotate(comments_count=Count('comments'), likes_count=Count('likes'))
        .get(slug=slug)
    )
    
    comments = post.comments.select_related("author")
    serialized_comments = [{
        'text': comment.text,
        'published_at': comment.published_at,
        'author': comment.author.username,
    } for comment in comments]

    most_popular_tags = Tag.objects.annotate(posts_count=Count('posts')).order_by('-posts_count')[:5]
    most_popular_posts = (
        Post.objects.popular()
        .prefetch_related("tags", "author")
        .annotate(comments_count=Count('comments'))[:5]
    )
    
    serialized_post = {
        'title': post.title,
        'text': post.text,
        'author': post.author.username,
        'comments': serialized_comments,
        'likes_amount': post.likes_count,
        'image_url': post.image.url if post.image else None,
        'published_at': post.published_at,
        'slug': post.slug,
        'tags': [serialize_tag(tag) for tag in post.tags.all()],
    }
    
    context = {
        'post': serialized_post,
        'popular_tags': [serialize_tag(tag) for tag in most_popular_tags],
        'most_popular_posts': [serialize_post(post) for post in most_popular_posts],
    }
    return render(request, 'post-details.html', context)


def tag_filter(request, tag_title):
    tag = Tag.objects.annotate(posts_count=Count('posts')).get(title=tag_title)
    
    most_popular_tags = Tag.objects.annotate(posts_count=Count('posts')).order_by('-posts_count')[:5]
    most_popular_posts = (
        Post.objects.popular()
        .prefetch_related("tags", "author")
        .annotate(comments_count=Count('comments'))[:5]
    )
    
    related_posts = (
        tag.posts.annotate(comments_count=Count('comments'))
        .prefetch_related("tags", "author")[:20]
    )
    
    context = {
        'tag': tag.title,
        'popular_tags': [serialize_tag(tag) for tag in most_popular_tags],
        'posts': [serialize_post(post) for post in related_posts],
        'most_popular_posts': [serialize_post(post) for post in most_popular_posts],
    }
    return render(request, 'posts-list.html', context)


def contacts(request):
    return render(request, 'contacts.html', {})
