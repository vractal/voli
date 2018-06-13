from django.test import TestCase
from model_mommy import mommy



# Test Recipe Model

class RecipeModelTest(TestCase):
    """ Tests for the recipe class """

    def setUp(self):
        self.recipe = mommy.make('core.Recipe')

    def test_str_representation(self):
        """ String representation must be model's name """
        self.assertEqual(str(self.recipe),self.recipe.name)


# test Tag Model

class TagModelTest(TestCase):
    """ Tests for the recipe class """

    def setUp(self):
        self.tag = mommy.make('core.Tag')

    def test_str_representation(self):
        """ String representation must be model's name """
        self.assertEqual(str(self.tag),self.tag.name)


class HomeTest(TestCase):
    """ Tests for homepage requests and content """

    def setUp(self):
        self.recipe = mommy.make('core.Recipe')
        self.recipe2 = mommy.make('core.Recipe')
        self.response = self.client.get('/')

    def test_get(self):
        """ Get '/' must return 200 code"""
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




