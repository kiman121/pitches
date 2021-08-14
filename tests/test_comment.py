import unittest
from app.models import Comment, User


class CommentModelTest(unittest.TestCase):
    '''
    Class to test the behaviours of the Comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.user_John = User(first_name='John', other_names='Pemba Mwadime',
                              username='pmwadime', email='pemba@ms.com')
        self.new_comment = Comment(
            1, self.user_John.id, 'What an amaizing picth!', '10/03/2017 07:29:46 -0700')
    
    def tearDown(self):
        '''
        Method that cleans up afetr every test case run
        '''
        Comment.query.delete()
        User.query.delete()

    def test_instance(self):
        '''
        Method that checks if the Comment instance is created
        '''
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_check_instance_variables(self):
        '''
        Method that checks the instance variables
        '''
        self.assertEquals(self.new_comment.post_id, 1)
        self.assertEquals(self.new_comment.user_id, self.user_John.id)
        self.assertEquals(self.new_comment.comments, 'What an amaizing picth!')
        self.assertEquals(self.created_at, '10/03/2017 07:29:46 -0700')

    def test_save_comment(self):
        '''
        Method that checks if the comment instance has been saved
        '''
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

    def test_get_comment_by_id(self):
        '''
        Method that checks if records are retrieved by post id
        '''
        self.new_comment.save_comment()
        got_comments = Comment.query.all()
        self.assertTrue(len(got_comments)>0)