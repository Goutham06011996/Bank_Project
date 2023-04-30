from .models import  Branch, Account
from django import forms


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)
        self.fields['branch'] = forms.ModelChoiceField(queryset=Branch.objects.all().order_by('name'),
                                                       empty_label='Select Branch')
        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
