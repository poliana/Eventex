"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

 
class HomepageUrlTest(TestCase):
    def test_sucess_when_get_homepage(self):
        response = self.client.get('/')
        self.assertEquals(200, response, status_code)
        self.assertTemplateUsed(response, 'index.html')
        """
        Tests that 1 + 1 always equals 2.
        """
    
