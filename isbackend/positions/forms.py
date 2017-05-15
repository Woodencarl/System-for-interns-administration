from django import forms
from .models import Position
from django.utils.translation import ugettext_lazy as _


class PosForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = ('mentor_name', 'division', 'pros_of_mentor', 'position_name', 'position_description', 'project',
                  'benefit_for_intern', 'requirements', 'notes')

        labels = {
            'mentor_name': _('Jméno a přijmení Mentora'),
            'division': _('Divize Mentora'),
            'pros_of_mentor': _('Čím je výjmečný mentor a jeho tým?'),
            'position_name': _('Název pozice'),
            'position_description': _('Popis pozice'),
            'project': _('Projekt'),
            'benefit_for_intern': _('Přínosy pro stážistu'),
            'requirements': _('Požadavky na stážistu'),
            'notes': _('Poznámky')
        }

    def __init__(self, *args, **kwargs):
        super(PosForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            if field != 'mentor_name' and field != 'division':
                self.fields[field].widget.attrs.update({
                    'required': self.fields[field].required,
                    'class': 'form-control',
                    'rows': '4',
                })
            else:
                self.fields[field].widget.attrs.update({
                    'required': self.fields[field].required,
                    'class': 'form-control col-md-7 col-xs-12',
                })

