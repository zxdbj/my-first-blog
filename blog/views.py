from django.shortcuts import render

# Create your views here.
def post_list(request):
    # 视图的逻辑
    return render(request, 'blog/post_list.html', {})