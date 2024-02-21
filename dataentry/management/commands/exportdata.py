import datetime
from django.core.management.base import BaseCommand
import csv

from django.apps import apps

# Proposed command - python manage.py exportdata model_name

class Command(BaseCommand):
    help = 'Export data from student model to a CSV file'

    def add_arguments(self,parser):#parser will allow us to write the extra arguments front of the command 
        parser.add_argument('model_name',type=str,help='Model name')

    def handle(self, *args, **kwargs):
        model_name=kwargs['model_name'].capitalize() #which is coming from the command model_name

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
            self.stderr(f'Model "{model_name}" could not found')
            return #returns the error and stops
        
        # fetch the data from the database
        data=model.objects.all()
        
        #generate the timestamp of current data and time
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        #define the file path/name
        file_path=f'exported_{model_name}_data_{timestamp}.csv'
        # print(file_path)

        #open csv file and the write the data
        with open(file_path,'w',newline='')as file: #after each line it is going to print in newline
            writer=csv.writer(file)

            #write the csv header
            #we want to print the field names of the model that we are trying to export 
            writer.writerow([field.name for field in model._meta.fields]) #it is going to give all field names whether it is an student model,customer

            #write data rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields]) 

        self.stdout.write(self.style.SUCCESS('Data exported successfully!'))