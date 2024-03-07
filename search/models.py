from django.db import models 

class SearchTerm(models.Model): 
    searched = models.CharField(max_length=50) 
    search_date = models.DateTimeField(auto_now_add=True) 
    
    def __name__(self):
        return self.searched
