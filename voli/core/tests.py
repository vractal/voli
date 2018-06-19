from django.test import TestCase
from model_mommy import mommy
from .models import Tag, Recipe


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
        self.tag = Tag.objects.create(name="Comida")
        self.tag2 = Tag.objects.create(name="Batata")
        self.recipe = mommy.make('core.Recipe')
        self.recipe2 = mommy.make('core.Recipe')
        self.recipe.tags.add(self.tag)
        self.recipe2.tags.add(self.tag)
        self.response = self.client.get('/')

    def test_get(self):
        """ Get '/' must return 200 code"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """ Must use home.html template """
        self.assertTemplateUsed(self.response, 'home.html')


    def test_context_has_recipes_list(self):
        """ Context must have 'recipes' entry with list of Recipe objects"""

        self.recipes = self.response.context['recipes']
        self.assertIsInstance(self.recipes[0],type(self.recipe))


    def test_context_has_tags_list(self):
        """ Context must have 'recipes' entry with list of Recipe objects"""

        self.tags = self.response.context['tags']
        self.assertIsInstance(self.tags[0],type(self.tag))



    def test_html(self):
        """ Html must contain required content"""
        requirements = [('<section id="receitas"', 1),
                        ('class="recipe', 2),
                        ('<input id="tag',2),
                        ('section id="tags',1),
                        ('<span class="tag',2)]

        for content, number in requirements:
            with self.subTest(content=content, number=number):
                self.assertContains(self.response, content, number)

    def test_recipes_pagination_until_limit(self):
        """ Must show one article per recipe in db (max to 20 per page)"""
        Tag.objects.all().delete()
        Recipe.objects.all().delete()
        limit = 14
        for number in range(0,(limit + 1),4):
            while len(Recipe.objects.all()) < number:
                mommy.make('core.Recipe', _fill_optional=True)
                mommy.make('core.Recipe', _fill_optional=True)
                mommy.make('core.Recipe', _fill_optional=True)
                mommy.make('core.Recipe', _fill_optional=True)
                response = self.client.get("/")
                with self.subTest(msg="numbers below page limit", number=number):
                    self.assertContains(response,'<article class="recipe',number)

        with self.subTest(msg="Number beyond pagination limit - should show only {}".format(limit)):
            mommy.make('core.Recipe', _fill_optional=True)
            mommy.make('core.Recipe', _fill_optional=True)
            response = self.client.get("/")
            self.assertContains(response, '<article class="recipe', limit)

# How to test if pagination is working as it should? (showing all instances and only once)

    def test_post(self):
        Tag.objects.all().delete()
        Recipe.objects.all().delete()
        tag = Tag.objects.create(name="Comida")
        recipe = mommy.make('core.Recipe')
        recipe2 = mommy.make('core.Recipe')
        recipe3 = mommy.make('core.Recipe')
        recipe.tags.add(tag)
        recipe2.tags.add(tag)
        post_resp = self.client.post("/",data={'tag':'Comida'})
        recipes = post_resp.context['recipes']
        self.assertEqual(len(recipes),len(tag.recipes.all()))


