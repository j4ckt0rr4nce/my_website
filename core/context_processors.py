from .models import Comment

def comment_no(request):
    c_no_1 = Comment.objects.filter(blog_no='Blog_1').count()
    c_no_2 = Comment.objects.filter(blog_no='Blog_2').count()
    c_no_3 = Comment.objects.filter(blog_no='Blog_3').count()

    context = {
	'c_no_1':c_no_1,
    'c_no_2':c_no_2,
    'c_no_3':c_no_3,
	}

    return context

