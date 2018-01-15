from django import forms
from django.forms import ModelForm, Textarea, ModelChoiceField, ImageField, CharField, FileInput, SelectDateWidget
from Blog.models import *
from django.utils.translation import ugettext_lazy as _
import datetime


class NewsForm(ModelForm):
    title = CharField(max_length=128, required=True)
    text = CharField(max_length=255, required=True,
                     widget=Textarea(attrs={'cols': 30, 'rows': 10}))
    attachment = ImageField(label=_('Pic'),required=False,
                            widget=FileInput)
    category = ModelChoiceField(queryset=Category.objects.all().order_by('name'),
                                empty_label=None)

    class Meta:
        model = News
        fields = ['title', 'text', 'attachment', 'category']
        labels = {
            'title': _('Title'),
            'text': _('Text'),
            'category': _('Category'),
            'attachment': _('Attachment')
        }


ACTIONS = [('publish', 'Publish'), ('reject', 'Reject')]


class ModerateForm(forms.Form):
    actions = forms.ChoiceField(label=_('Actions'), choices=ACTIONS, widget=forms.RadioSelect(), initial=ACTIONS[0][0])
    comment = CharField(max_length=255, required=False, widget=Textarea(attrs={'cols': 30, 'rows': 10}))


CHOICES = [('category', 'By Category'),
           ('pub_date', 'By Publication Date')
           ]


class SearchForm(forms.Form):
    options = forms.ChoiceField(label=_('Options'), choices=CHOICES, widget=forms.RadioSelect(), initial=CHOICES[0][0])
    category = ModelChoiceField(label=_('Category'), queryset=Category.objects.all().order_by('name'),
                                empty_label=None)
    pub_date = forms.DateField(label=_('Date'),widget=SelectDateWidget(years=range(2017, datetime.datetime.now().year + 1)))
