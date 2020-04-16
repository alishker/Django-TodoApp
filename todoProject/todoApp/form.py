from django.forms import ModelForm
from .models import Tasks


# Create the form class.
class TodoForm(ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
