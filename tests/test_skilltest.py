from skilltest import app, db
import skilltest
import unittest


TEST_DB = 'test.db'


class TestApp(unittest.TestCase):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' +  TEST_DB
    TESTING = True

    @classmethod
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' +  TEST_DB
        self.app = app.test_client()
        db.create_all()


    @classmethod
    def tearDown(self):
        db.session.remove()
        db.drop_all()
 

    def test_db_insert(self):
        """
        Validate entry of user in database
        """
        skilltest.create_user('2wgerbe43546')
        queryId = skilltest.User.query.filter_by(amazonId='2wgerbe43546').first()
        self.assertEqual(queryId.amazonId, '2wgerbe43546')


if __name__ == '__main__':
    unittest.main()
