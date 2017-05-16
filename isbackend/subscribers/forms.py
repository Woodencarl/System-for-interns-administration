from django import forms
from .models import Subscriber
from django.utils.translation import ugettext_lazy as _
from .models import OBLIGATION_LIST
from .models import INTEREST_LIST


class NewsFrom(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('first_name', 'last_name', 'e_mail', 'phone', 'school', 'year',
                  'obligation', 'interests', 'other', 'agreement')
        labels = {
            'first_name': _('Jméno'),
            'last_name': _('Příjmení'),
            'date_of_birth': _('Datum narození'),
            'e_mail': _('E-mail'),
            'phone': _('Telefon'),
            'school': _('Škola'),
            'year': _('Ročník'),
            'obligation': _('Úvazek'),
            'interests': _('Zájem o'),
            'agreement': _('Souhlas'),
        }

    def __init__(self, *args, **kwargs):
        super(NewsFrom, self).__init__(*args, **kwargs)
        placeholders = {
            'first_name': _('Bruce'),
            'last_name': _('Wayne'),
            'date_of_birth': _('1999-12-24'),
            'e_mail': _('bruce@wayne.gc'),
            'phone': _('314 159 265'),
            'school': _('Česká vysoká škola v Gotham City'),
            'year': _('2. ročník'),
            'other': _('Jiné'),
            'agreement': _('Prosíme zaškrtnout'),
        }
        self.fields['e_mail'].required = True
        # self.fields['agreement'].required = True
        for field in self.fields.keys():
            if field != 'obligation' and field != 'interests':
                self.fields[field].widget.attrs.update(
                    {'required': True, 'placeholder': placeholders[field],
                     'class': 'form-control col-md-7 col-xs-12'})

    obligation = forms.MultipleChoiceField(label='Úvazek', required=False, choices=OBLIGATION_LIST,
                                           widget=forms.CheckboxSelectMultiple(
                                               attrs={'class': 'flat', 'style': 'list-style:none;'}))
    interests = forms.MultipleChoiceField(label='Zájem o', required=False, choices=INTEREST_LIST,
                                          widget=forms.CheckboxSelectMultiple(attrs={'class': 'flat'}))
    other = forms.CharField(label='Jiné', required=False, max_length=100)

    agreement = forms.BooleanField(label='Souhlas', help_text='Souhlas se zpracováním osobních údajů', required=True,
                                   widget=forms.CheckboxInput(attrs={'class': 'checkbox flat'}))
