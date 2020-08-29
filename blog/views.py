from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from .forms import CommentForm
# from django.contrib.auth.decorators import login_required
from .models import Comment
# from django.utils import timezone
# from django.contrib.auth.models import User
from django.core.paginator import Paginator
# Create your views here.


# def home(request):
#     context = {
#         'posts': Post.objects.all(),
#         'title': 'DJ'
#     }
#     return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # default: <app>/<model>_<viewtype>.html
    # context_object_name = 'post_list' # default: object_list for listview, object for detailview
    ordering = ['-date_posted']  # default old to new, -date_posted orders them from new to old
    paginate_by = 2



class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'tag', 'content']
    # success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)


# def comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your comment has been saved')
#             return redirect('home')
#     else:
#         form = CommentForm()
#     context = {'form': form, }
#     return render(request, 'blog/comment.html', context)


class CommentDetailView(DetailView):
    model = Comment


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['comment']
    # success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentListView(ListView):
    model = Comment
    # template_name = 'blog/home.html' # default: <app>/<model>_<viewtype>.html
    # context_object_name = 'post_list' # default: object_list for listview, object for detailview
    ordering = ['-id']  # default old to new, -date_posted orders them from new to old


########################################################
# TEST FIELD ## WILL BE DELETED LATER



