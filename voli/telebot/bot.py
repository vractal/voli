from telegram.ext import Updater, CommandHandler
from voli.core.models import Recipe, Tag
from django.db import IntegrityError
from .token import token
import re


updater = Updater(token=token)

dispatcher = updater.dispatcher

def start(bot,update):

    bot.send_message(chat_id=update.message.chat_id,text="Oi {}, eu sou seu bot!".format(update.effective_user["first_name"] ))


def receita(bot,update):
    """ Manipulates input from command 'receita' """

    input_text = update.message.text[8:]

    if len(input_text) > 0:
        r = re.search(r'^\s*(?P<url>\S*)\s*(?P<name>.*?)\s*(?P<tags>#.*)?$', input_text)
        if r.group('tags'):
            tags = set(r.group('tags').replace(" ", "").split("#"))
            tags = [t for t in tags if t]
        else:
            tags = []

        try:
            recipe = Recipe.objects.create(origin_url=r.group('url'),name=r.group('name'))
            for t in tags:
                try:
                    tag = Tag.objects.create(name=t)
                except IntegrityError:
                    tag = Tag.objects.get(name=t)

                recipe.tags.add(tag)

            text = "Anotado!\n Nome: {} \n Url: {} \n Tags: {}".format(recipe.name,
                                                                       recipe.origin_url,
                                                                       ", ".join(tags))
        except IntegrityError:
            try:
                recipe = Recipe.objects.get(origin_url=r.group('url'))
                text = "Você provavelmente já adicionou essa receita antes!\n Nome: {} \n Url: {} \n Tags: {}".format(
                                                                                                                recipe.name,
                                                                                                                recipe.origin_url,
                                                                                                                ", ".join(tags))
            except:
               text = "Parece que algo saiu mal..."
    else:
        text="Parece que você não escreveu nada... \n Escreva assim (tudo separado por espaços):\n" \
             "<comando> <link da receita> <nome(opicional)> <tags(opcional). " \
             "\nex: /receita presveg.com/batata-linda  batata maravilhosa  #batata #veg #larica"

    bot.send_message(chat_id=update.message.chat_id, text=text)



start_handler = CommandHandler("start",start)
dispatcher.add_handler(start_handler)

receita_handler = CommandHandler("receita",receita)
dispatcher.add_handler(receita_handler)
