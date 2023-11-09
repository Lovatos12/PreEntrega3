from django import forms

class ForoFormulario(forms.Form):
  
    nombre = forms.CharField(
        required=True,
        label="Nombre del foro",
        help_text="Ingrese el nombre del foro",
    )
    tema = forms.ChoiceField(
        choices=[("Comida", "Comida"), ("Salud", "Salud"), ("Ejercicio", "Ejercicio"), ("Otro", "Otro")],
        label="Tema del foro",
        help_text="Seleccione el tema del foro",
    )
    contenido = forms.CharField(
        required=True,
        label="Contenido del foro",
        help_text="Ingrese el contenido del foro",
    )
    
class ForistaFormulario(forms.Form):
  
    nombre = forms.CharField(
        required=True,
        label="Nombre",
        help_text="Ingrese el nombre de forista",
    )
    apellido = forms.CharField(
        required=True,
        label="Apellido",
        help_text="Ingrese el apellido del forista",
    )    
    sexo = forms.ChoiceField(
        choices=[("M", "Masculino"), ("F", "Femenino")],
        label="sexo",
        help_text="Seleccione sexo",
    )
    email = forms.EmailField(
        required=False,
        label="email",
        help_text="Ingrese email"
    )
    dni = forms.CharField(
        max_length=32,
        label="dni",
        help_text="Ingrese DNI"
    )
    fecha_nacimiento = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'}),
        help_text="Ingrese Fecha de nacimiento"
    )