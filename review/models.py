from django.db import models

class CodePost(models.Model):
    LANGUAGE_CHOICES = [
        ('py', 'Python'),
        ('c', 'C'),
        ('cpp', 'C++'),
        ('js', 'JavaScript'),
        ('java', 'Java'),
        # add more as needed
    ]

    title = models.CharField(max_length=200)
    code = models.TextField()
    description = models.TextField(blank=True)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    author_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(CodePost, on_delete=models.CASCADE, related_name='comments')
    commenter_name = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter_name} on {self.post.title}"
