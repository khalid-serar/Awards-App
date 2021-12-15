from golden.models import Profile, Project, Reviews
from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

#class Profile Test
class TestProfile(TestCase):
    def setUp(self):
        '''
        test case for profiles
        '''
        self.user = User(username='mylo')
        self.user.save()
        self.profile = Profile(profile_picture='orange and yellow',profile_bio='test bio',profile_contact="0111111111",user=self.user)
        self.profile.save_profile()

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

# class Project Test
class TestProject(TestCase):
    def setUp(self):
        self.project = Project(project_title ='new project', project_image='image.url',project_description="project",project_link="http://www.awwaards.com")

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_save_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.project.save_project()
        projects = Project.objects.all()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)==0)

#class Reviews/Rates Test
class TestReviews(TestCase):
    def setUp(self):
       
        self.user = User(username='mylo')
        self.user.save()
        self.project = Project(project_title ='new project', project_image='image.url',project_description="project",project_link="http://www.awwaards.com")
        self.project.save_project()

        self.new_review=Reviews(design="1",usability="2",content="3",user=self.user,project=self.project)
        self.new_review.save_review()

    def tearDown(self):
        Reviews.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_review,Reviews))

    def test_save_review(self):
        reviews = Reviews.objects.all()
        self.assertTrue(len(reviews)>0)

    def test_delete_review(self):
        self.new_review.save_review()
        self.new_review.delete_review()
        reviews = Reviews.objects.all()
        self.assertTrue(len(reviews)==0)