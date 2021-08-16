from . import db
from .models import Post, PostDetails, Category, User, Comment, CommentDetails


def get_posts():
    '''
    Function that retrieves posts
    '''
    results = db.session.query(Post, Category, User). \
        select_from(Post).join(Category).join(User).all()

    comments = get_comments()

    post_details = []

    for post, category, user in results:
        post_id = post.id
        post_date = post.created_at
        post_detail = post.post
        category = category.category_name
        posted_by = user.first_name+" "+user.other_names
        profile_pic_path = user.profile_pic_path
        
        # post_comments = []

        # if comments:
        #     for comment in comments:
        #         if comment['post_id'] == post_id:
        #             post_id = comment['post_id']
        #             comment_date = comment['comment_date']
        #             commented_by = comment['commented_by']
        #             profile_pic_path = comment['profile_pic_path']
        #         post_comments.append({'post_id':post_id,'comment_date':comment_date, 'commented_by':commented_by,'profile_pic_path':profile_pic_path})

        post_detail_object = PostDetails(
            post_id, post_date, post_detail, category, posted_by, profile_pic_path)
        post_details.append(post_detail_object)
    return post_details

def get_comments():
    '''
    Function that retrieves comments
    '''
    results = db.session.query(Comment, User, Post). \
        select_from(Comment).join(User).join(Post).all()

    comments = []

    for comment, user, post in results:
        post_id = comment.post_id
        comment_date = comment.created_at
        commented_by = user.first_name+" "+user.other_names
        profile_pic_path = user.profile_pic_path

        comments_object = CommentDetails(post_id, comment_date,commented_by,profile_pic_path)
        comments.append(comments_object)
    
    return comments