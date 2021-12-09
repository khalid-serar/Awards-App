from django.db import models

# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    profile_picture = CloudinaryField('image')
    profile_bio = models.TextField()
    profile_contact = models.CharField(max_length=60,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile",primary_key=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Project(models.Model):
    project_title = models.CharField(max_length=60,blank=True)
    project_image = CloudinaryField('image')
    project_description = models.TextField()
    project_link = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.project_title

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def project_by_id(cls,id):
        project = Project.objects.filter(id =id)
        return project

    @classmethod
    def search_by_project_title(cls,search_term):
    	projects = cls.objects.filter(project_title__icontains=search_term)
    	return projects

class Reviews(models.Model):
    REVIEW_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    usability = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    content = models.IntegerField(choices=REVIEW_CHOICES,default=0,blank=False)
    average =  models.DecimalField(default=1,blank=False,decimal_places=2,max_digits=100)
    project = models.ForeignKey(Project,null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def save_review(self):
        self.save()

    def delete_review(self):
        self.delete()





