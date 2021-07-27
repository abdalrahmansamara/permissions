from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_post = Post.objects.create(
            name = 'food',
            time_to_prepare = 45,
            serving = 5,
            instructions = "not available",
            ingredients = 'no',
            posted_by = test_user,
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        posted_by = str(post.posted_by)
        ingredients = str(post.ingredients)
        name = str(post.name)
        self.assertEqual(posted_by, 'testuser')
        self.assertEqual(ingredients, 'no')
        self.assertEqual(name, 'food')
        self.assertEqual(post.time_to_prepare, 45)
        self.assertEqual(post.serving, 5)
        self.assertEqual(post.instructions, "not available")