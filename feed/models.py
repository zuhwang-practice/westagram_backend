from django.db import models

class Comment(models.Model):
    user      = models.ForeignKey('account.User', on_delete = models.CASCADE,
                                  related_name = 'commant_author')
    comment   = models.TextField()
    like      = models.IntegerField(verbose_name = 'likes', null = True)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'comments'

# ! 피드의 사진이 여러장일 수 있기 때문에 이미지테이블을 따로 생성하여 관리하야 여러장의 사진을 넣을 수 있다.
class Feed(models.Model):
    user         = models.ForeignKey('account.User', on_delete = models.CASCADE, related_name = 'author')
    # ? user, user_profile이 1:1일때 굳이 user_profile컬럼을 추가할 필요없다..! 
    # user_profile = models.ForeignKey('account.UserProfile', on_delete = models.SET_NULL, null = True, related_name = 'avatar')
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