from . import db
from sqlalchemy import desc
from .models import Post, PostDetails, Category, User, Comment, CommentDetails


def get_posts():
    '''
    Function that retrieves posts
    '''
    results = db.session.query(Post, Category, User). \
        select_from(Post).join(Category).join(User).order_by(desc(Post.id)).all()

    comments = get_comments()

    post_details = []

    for post, category, user in results:
        post_id = post.id
        post_date = post.created_at
        post_detail = post.post
        category = category.category_name
        posted_by = user.first_name+" "+user.other_names
        profile_pic_path = user.profile_pic_path
        upvote = post.upvote
        downvote = post.downvote
        
        post_comments_count = []

        count = 0;
        if comments:
            for comment in comments:
                if comment.post_id == post_id:
                    count +=1

        post_detail_object = PostDetails(
            post_id, post_date, post_detail, category, posted_by, profile_pic_path, count, upvote, downvote)
        post_details.append(post_detail_object)
        count = 0;
    return post_details

def get_comments():
    '''
    Function that retrieves comments
    '''
    results = db.session.query(Comment, User). \
        select_from(Comment).join(User).all()

    comments = []

    for comment, user in results:
        post_id = comment.post_id
        comments_made = comment.comments
        comment_date = comment.created_at
        commented_by = user.first_name+" "+user.other_names
        profile_pic_path = user.profile_pic_path

        comments_object = CommentDetails(post_id, comments_made, comment_date,commented_by,profile_pic_path)
        comments.append(comments_object)

    return comments