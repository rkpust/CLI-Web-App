from django.shortcuts import render
from .models import Command
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt  # Use @csrf_exempt for simplicity in development. For production, consider using CSRF tokens.
def index(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON body
            input_text = data.get('userInput')  # Get the 'userInput' field
            
            # Process the input (you can add your own logic here)
            output_text = execute_command(input_text)

            return JsonResponse({'response': output_text})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return render(request, 'index.html')


def execute_command(command):
    # Here you can define how to handle the command input
    # For simplicity, let's just echo the command
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout
    error = result.stderr
    print(output)
    print(result.returncode)


    # Check if there was an error
    if result.returncode == 0 or result.returncode == 1:
        if output == "":
            return f"{error}"
        else:
            return f"{output}"
        # return  f"{output}" + f"{error}"
        



def current_path_command():
    # Here you can define how to handle the command input
    # For simplicity, let's just echo the command
    result = subprocess.run('cd', shell=True, capture_output=True, text=True)
    output1 = result.stdout
    return f'{output1}'
