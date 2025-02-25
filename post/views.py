from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .form import CreatePostForm, UpdatePostForm, ImageForm, DocumentForm
from django.views.decorators.csrf import csrf_protect

from django.utils.translation import activate, gettext_lazy as _
from.models import Post, Image, Document

# ceate post
@csrf_protect
def create_post(request):
    activate('ar')
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.save()
            messages.info(request, _('Post created successfully.'))
            return redirect('post:index')
        else:
            messages.error(request, _('Failed to create post.'))
            return redirect('post:create_post')
    else:
        form = CreatePostForm()
    context = {'form': form}
    return render(request, 'post/create_post.html', context)


# view post details
def post_details(request, pk):
    activate('ar')
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request, 'post/post_details.html', context)

# update post
@csrf_protect
def update_post(request, pk):
    activate('ar')
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, _('Post updated successfully.'))
            return redirect('post:index')
        else:
            messages.error(request, _('Failed to update post.'))
            return redirect('post:update_post', pk=pk)
    else:
        form = CreatePostForm(instance=post)
    context = {'form': form, 'post': post}
    return render(request, 'post/update_post.html', context)


# delete post
@csrf_protect
def delete_post(request, pk):
    activate('ar')  # Set language to Arabic
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':  # Confirm deletion
        post.delete()
        messages.info(request, _('Post deleted successfully.'))
        return redirect('post:index')

    return render(request, 'post/delete_post.html', {'post': post})

# see all post that user created

@csrf_protect
def all_created_posts(request):
    activate('ar')
    posts = Post.objects.filter(created_by=request.user.id)
    context = {'posts': posts}
    return render(request, 'post/all_created_posts.html', context)
    

# homepage
@csrf_protect
def index(request):
    activate('ar')
    if request.user.is_authenticated:
        # Redirect authenticated users to their created posts
        return redirect ('post:all_created_posts')
    
    # For non-authenticated users, show a general list of posts
    posts = Post.objects.all()  # You can modify this to show only certain posts if needed
    context = {'posts': posts}
    return render(request, 'post/index.html', context)


def image_list(request):
    """ Show all images """
    images = Image.objects.all().order_by('-created_at')
    return render(request, 'post/image_list.html', {'images': images})


def add_image(request):
    activate('ar')
    """ Add a new image """
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Image uploaded successfully!"))
            return redirect('post:image_list')
        else:
            messages.error(request, _('Something went wrong!'))
            return redirect('post:add_image')    
    else:
        form = ImageForm()
    return render(request, 'post/image_form.html', {'form': form})

def delete_image(request, image_id):
    activate('ar')
    """ Delete an image """
    image = get_object_or_404(Image, id=image_id)
    image.delete()
    messages.success(request, _("Image deleted successfully!"))
    return redirect('post:image_list')


def document_list(request):
    """ Show all videos """
    documents = Document.objects.all().order_by('-created_at')
    return render(request, 'post/document_list.html', {'documents': documents})


def add_document(request):
    activate('ar')
    """ Add a new document """
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, _("Document uploaded successfully!"))
            return redirect('post:document_list')
        else:
            messages.error(request, _('Something went wrong'))
            return redirect('post:add_document')
    else:
        form = DocumentForm()
    return render(request, 'post/document_form.html', {'form': form})


def delete_document(request, document_id):
    activate('ar')
    """ Delete a video """
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    messages.success(request, _("Document deleted successfully!"))
    return redirect('post:document_list')

#def all_images(request):
   # """ Show all images """
   # images = Image.objects.all().order_by('-created_at')
   # return render(request, 'post/all_images.html', {'images': images})

#def all_documents(request):
    #""" Show all videos """
   # documents = Document.objects.all().order_by('-created_at')
    #return render(request, 'post/all_documents.html', {'documents': documents})