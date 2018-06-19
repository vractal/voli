from django.core.management.base import BaseCommand
from voli.telebot.bot import updater

class Command(BaseCommand):
    help="Start bot server in pooling mode"

    def handle(self,*args,**options):
        updater.start_polling()
