from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django.utils import timezone


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    excerpt = models.TextField(max_length=200, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = TaggableManager()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True
        )
    ingredients = models.TextField(max_length=5800, default="", blank=True)
    instructions = models.TextField(max_length=5800, default="", blank=True)
    preparation_time = models.DurationField()
    cooking_time = models.DurationField()
    portions = models.PositiveIntegerField(default=1)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
