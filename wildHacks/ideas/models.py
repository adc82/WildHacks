from django.core.urlresolvers import reverse
from django.db import models

class Idea (models.Model):
    """
    A class that represents a single start up idea
    """
    #A complete discrition of the start up idea
    long_discription = models.TextField(blank=False, max_length=1000)
    #The title of the idea 
    title = models.CharField(blank=False, max_length=100)
    #The short sort of "one sentence" discrition of the idea
    short_discription = models.TextField(blank=False, max_length=140)
    #A field that represents the numbers of upvotes a downvote is -1
    votes = models.IntegerField(default = 0)
    #Publication date
    pub_date = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    #Author of the idea
    creator = models.ForeignKey('users.User', null=True)

    def up_vote(self):
        votes += 1
        self.save()

    def down_vote(sel):
        votes -= 1
        self.save()

    def get_absolute_url(self):
        return reverse('ideas:detail', kwargs={'pk': self.pk})
    
