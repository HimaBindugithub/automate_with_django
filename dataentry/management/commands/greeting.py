#creating customcommand greeting

from django.core.management.base import BaseCommand


#proposed command=python mange.py greeting Bindu
#proposed output=Hii {name},Good Morning

class Command(BaseCommand):
    help="Greets the user" #this is a command level help text

    def add_arguments(self,parser):#parser will allow us to write the extra arguments front of this command python mange.py greeting
        parser.add_argument('name',type=str,help='Specifies user name')#here help text is used,this is a argument level help text,this name will be accessble from
      #from this handle method also because of **kwargs  
    def handle(self,*args,**kwargs):
        name=kwargs['name']
        greeting=f'Hii {name},Good Morning'#this is the final greeting,this greeting will go to the output below
        self.stdout.write(greeting)#to want this name dynamic,
        #to print any type of error
        #self.stderr.write(greeting) #output will be in red color
        
        #to print suceess message
        #self.stderr.write(self.style.SUCCESS(greeting) #output will be in green color

        #self.stderr.write(self.style.WARNING(greeting) #output will be in yellow color
