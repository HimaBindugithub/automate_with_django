from django.core.management.base import BaseCommand,CommandError

import csv

# from dataentry.models import Student

from django.apps import apps  #to import all apps

# Proposed command - python manage.py importdata file_path model_name

class Command(BaseCommand):
    help="Import data from the csv file" #this is a command level help text

    def add_arguments(self,parser):#parser will allow us to write the extra arguments front of the command 
        parser.add_argument('file_path',type=str,help='Path to the csv file')
        parser.add_argument('model_name',type=str,help='Name of the model')


    def handle(self,*args,**kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()#receives model name in handle fun

        #search fro the model across all installed apps
        model=None
        for app_config in apps.get_app_configs(): #we can loop through all apps,.get_app_config()
            #contains all meta data and can acess the labels

            #try to search for the model

            try:
                model=apps.get_model(app_config.label,model_name) #in order to get a model we are get_model()
                break #stop searching once the model is found
            except LookupError:
                continue #model not found in this app,continue searching in the next app 
    
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any app!')
        with open(file_path,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from csv successfully!'))   

        