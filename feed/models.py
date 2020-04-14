from django.db import models

# Create your models here.
# 피드
# 댓글


class Comment(models.Model):
    user      = models.ForeignKey('account.User', on_delete = models.CASCADE,
                                  related_name = 'commant_author')
    comment   = models.TextField()
    like      = models.IntegerField(verbose_name = 'likes', null = True)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'comments'


class Feed(models.Model):
    user         = models.ForeignKey('account.User', on_delete = models.CASCADE, related_name = 'author')
    user_profile = models.ForeignKey('account.UserProfile', on_delete = models.SET_NULL, null = True, related_name = 'avatar')
    image_url    = models.CharField(max_length = 300, verbose_name = 'image')
    content      = models.TextField(verbose_name = 'content')
    like         = models.IntegerField(verbose_name = 'likes', null = True)
    create_at    = models.DateTimeField(auto_now_add = True)
    update_at    = models.DateTimeField(auto_now = True)
    comment      = models.ManyToManyField('Comment', through = 'FeedComment', related_name = 'feed_comment')
    feed         = models.ManyToManyField('Feed', through = 'FeedComment', related_name = 'comment_feed')

    class Meta:
        db_table = 'feeds'

class FeedComment(models.Model):
    feed    = models.ForeignKey('Feed', on_delete = models.CASCADE, related_name = 'feed_id')
    comment = models.ForeignKey('Comment', on_delete = models.CASCADE, related_name = 'comment_id')

    class Meta:
        db_table = 'feed_comment'