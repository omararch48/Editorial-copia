from django import forms


class ContactMessageForm(forms.Form):
    SUBJECT_CHOICE = (
        ('0', 'Publicaciones'),
        ('1', 'Servicios editoriales'),
        ('2', 'Otro'),
    )
    name = forms.CharField(
        label='name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'id': 'name',
                'placeholder': 'Ingresa tu nombre (obligatorio)',
            }
        )
    )
    email = forms.EmailField(
        label='email',
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'email',
                'id': 'email',
                'placeholder': 'Ingresa tu email (opcional)',
            }
        )
    )
    phone = forms.CharField(
        label='phone',
        required=False,
        widget=forms.TextInput(
            attrs={
                'type': 'tel',
                'id': 'phone',
                'placeholder': 'Ingresa tu teléfono (opcional)',
            }
        )
    )
    subject = forms.ChoiceField(
        label='subject',
        required=True,
        choices=SUBJECT_CHOICE,
        widget=forms.Select(
            attrs={
                'type': 'text',
                'id': 'subject',
                'placeholder': 'Ingresa tu nombre (obligatorio)',
            }
        )
    )
    message = forms.CharField(
        label='message',
        required=False,
        widget=forms.Textarea(
            attrs={
                'type': 'text',
                'id': 'message',
                'placeholder': 'Ingresa tu nombre (obligatorio)',
                'rows': '3',
            }
        )
    )