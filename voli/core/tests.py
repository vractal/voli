from django.test import TestCase

# Create your tests here.

class HomeTest(TestCase):
    """ Tests HomePage"""

    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """ Get must return 200 code"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use home.html template """
        self.assertTemplateUsed(self.response, 'home.html')
        
    def test_html(self):
        """ Html must contain required content"""
        requirements = [('<section id="receitas"', 1),
                        ]

        for content, number in requirements:
            with self.subTest(content=content, number=number):
                self.assertContains(self.response, content, number)
        



