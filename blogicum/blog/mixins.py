from django.urls import reverse

from .models import Comment, Post


class PostsEditMixin:
    model = Post
    template_name = 'blog/create.html'


class CommentEditMixin:
    model = Comment
    pk_url_kwarg = 'comment_pk'
    template_name = 'blog/comment.html'

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.kwargs['post_id']])
