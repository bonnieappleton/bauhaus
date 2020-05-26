from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        required=True,
        label='Name*',
    )
    contact_email = forms.EmailField(
        required=True,
        label='Email*',
    )
    email_content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label='Your message*',
    )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
