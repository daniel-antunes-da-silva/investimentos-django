from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# criando nova classe que herda da UserCreatinForm, para não precisar recriar
# toda funcionalidade que já existe. Dessa forma, é possível criar novos campos.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']