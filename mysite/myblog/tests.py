from django.test import TestCase
from django.contrib.auth.models import User
from myblog.models import Post
from myblog.models import Category
import datetime 
from django.utils.timezone import utc

class PostTestCase(TestCase):
    fixtures = ['myblog_test_fixture.json',]

    def setUp(self):
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)

class CategoryTestCase(TestCase):

    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)

class FrontEndTestCase(TestCase):
    '''test views provided in the front-end'''
    fixtures - ['myblog_test_fixture.json', ]

    def setUp(self):
        self.now = datetime.date.utcnow().replace(tzinfo=utc)
        self.timedelta = datetime.timedelta(15)
        author = User.objects.get(pk=1)
        for count in range(1, 11):
            post = Post(title="Post %d Title" % count,
                        text="foo",
                        author=author)
            if count < 6:
                #publish the first five posts
                pubdate = self.now - self.timedelta * count
                post.published_date = pubdate
            post.save()


# Create your tests here.
