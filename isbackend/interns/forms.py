from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Intern
from .models import Comments
from positions.models import Position
from django.utils.timezone import datetime


class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = ('first_name', 'last_name', 'date_of_birth', 'e_mail', 'phone', 'school', 'faculty', 'year',
                  'field', 'interests', 'learned_from', 'resume', 'cover_letter')
        # exclude = ('resume','cover_letter') #exclude from form

        labels = {
            'first_name': _('Jméno'),
            'last_name': _('Příjmení'),
            'date_of_birth': _('Datum narození'),
            'e_mail': _('E-mail'),
            'phone': _('Telefon'),
            'school': _('Škola'),
            'faculty': _('Fakulta'),
            'year': _('Ročník'),
            'field': _('Zaměření'),
            'wanted_boarding_date': _('Chtěný datum nástupu'),
            'interests': _('Zájem o'),
            'learned_from': _('Vím o programu'),
            'resume': _('Životopis'),
            'cover_letter': _('Motivační dopis'),
        }

    def __init__(self, *args, **kwargs):

        super(InternForm, self).__init__(*args, **kwargs)
        placeholders = {
            'first_name': _('Bruce'),
            'last_name': _('Wayne'),
            'date_of_birth': _('1999-12-24'),
            'e_mail': _('bruce@wayne.gc'),
            'phone': _('314 159 265'),
            'school': _('Česká vysoká škola v Gotham City'),
            'faculty': _('Fakulta bojových umění'),
            'year': _('2. ročník'),
            'wanted_boarding_date': _(datetime.today()),
            'field': _('Tajemné zmizení a vyvolání strachu'),
            'interests': _('Zájmy'),
            'learned_from': _('Vím o programu'),
            'resume': _('Životopis'),
            'cover_letter': _('Motivační dopis'),
        }

        for field in self.fields.keys():
            if field != 'resume' and field != 'cover_letter':
                self.fields[field].widget.attrs.update({
                    'required': self.fields[field].required,
                    'placeholder': placeholders[field],
                    'class': 'form-control col-md-7 col-xs-12'
                })
        self.fields['interests'].queryset = Position.objects.filter(is_active=True)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)


class EditFrom(forms.ModelForm):
    class Meta:
        model = Intern
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'date_of_birth', 'e_mail', 'phone', 'school', 'faculty', 'year',
                  'field', 'position', 'mentor', 'division', 'first_interview_date', 'second_interview_date',
                  'contract_till', 'assigned_coordinator', 'status', 'learned_from',)

    def _get_validation_exclusions(self):
        exclude = ['__all__']
