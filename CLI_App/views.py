from django.shortcuts import render
from .models import Command
import subprocess

# Create your views here.
def index(request):
    input_text = 'cd'
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        output_text = execute_command(input_text)
        Command.objects.create(input_text=input_text, output_text=output_text)
        currect_path = current_path_command()
    else:
        input_text = ''
        output_text = ''
        
        # current_path_command()
        # Command.objects.create(input_text='cd', output_text=output_text)
        currect_path = current_path_command()

    context = {
        'currect_path': currect_path,
        'input_text': input_text,
        'output_text': output_text
    }
    return render(request, 'index.html', context)

def execute_command(command):
    # Here you can define how to handle the command input
    # For simplicity, let's just echo the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout
    return f'{output}'



def current_path_command():
    # Here you can define how to handle the command input
    # For simplicity, let's just echo the command
    result = subprocess.run('cd', shell=True, capture_output=True, text=True)
    output1 = result.stdout
    print(output1)
    return f'{output1}'
