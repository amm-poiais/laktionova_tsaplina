from django.forms import ModelForm, Textarea, ModelChoiceField, ImageField, CharField, FileInput,ChoiceField
from Blog.models import *
from django.utils.translation import ugettext_lazy as _


class NewsForm(ModelForm):
    title = CharField(max_length=128, required=False)
    text = CharField(max_length=255, required=False,
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

