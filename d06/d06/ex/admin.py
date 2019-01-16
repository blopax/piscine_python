from django.contrib import admin
from .models import TipUser, Upvotes, Downvotes, Tip

# Register your models here.
class TipUserAdmin(admin.ModelAdmin):
    pass

class UpvotesAdmin(admin.ModelAdmin):
    pass

admin.site.register(TipUser, TipUserAdmin)



#
# class Downvotes(models.Model):
#     vote_user = models.CharField(max_length=128)
#
#
# class Tip(models.Model):
#     content = models.TextField()
#     author = models.CharField(max_length=128)
#     date = models.DateTimeField(auto_now_add=True)
#     upvotes = models.ManyToManyField(Upvotes)
#     downvotes = models.ManyToManyField(Downvotes)

