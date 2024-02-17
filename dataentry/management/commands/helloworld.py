#creating customcommand helloworld

from django.core.management.base import BaseCommand

class Command(BaseCommand): # Here Command iherits all features attributes and methods from the BaseCommand
    help="Prints Hello World"  #help is a attribute assigned an message to it
    def handle(self,*args,**kwargs):
        #we write the logic
        self.stdout.write('Hello World')
