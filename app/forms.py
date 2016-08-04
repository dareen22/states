from django.core.urlresolvers import reverse 
from django import forms 
from django.core.validators import RegexValidator

from models import State, City

# crispy import:

from crispy_forms.helper import FormHelper 
from crispy_forms.layout import Submit 
from crispy_forms.layout import Layout, Submit, HTML, Div, Field 
from crispy_forms.bootstrap import FormActions 

class CreateState(forms.ModelForm):
    class Meta:
        model = State 
        fields = '__all__'

class EditState(forms.ModelForm):
    class Meta:
        model = State
        fields = '__all__'


class EditCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EditCity, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('edit_city', kwargs={'pk':self.instance.pk })
        #self.helper.add_input(Submit('submit', 'Search'))
        self.helper.layout = Layout(
                    Div('state', 'name', 'county', css_class='col-sm-6'),
                    Div('latitude', 'longitude', 'zipcode', css_class='col-sm-6'),
                    Div(FormActions(Submit('submit', 'Save')), css_class='col-sm-12')
            )
                    
                       


class CityCreate(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CityCreate, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'create_city'
        #self.helper.add_input(Submit('submit', 'Search'))
        self.helper.layout = Layout(
                    Div('state', 'name', 'county', css_class='col-sm-6'),
                    Div('latitude', 'longitude', 'zipcode', css_class='col-sm-6'),
                    Div(FormActions(Submit('submit', 'Save')), css_class='col-sm-12'),
            )
                        

class CitySearchForm(forms.Form):
    letters_only = RegexValidator(r'^[a-zA-Z]+$','Only letters are allowed')
    city = forms.CharField(required=True, initial='orem', validators=[letters_only])
    state = forms.CharField(required=True, initial='Utah', validators=[letters_only])



    def __init__(self, *args, **kwargs):
        super(CitySearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_action = 'city_search'
        #self.helper.add_input(Submit('submit', 'Search'))
        self.helper.layout = Layout(
                    Div('city', css_class='col-sm-5 col-md-5'), 
                    Div('state', css_class='col-sm-5 col-md-5'),
                    Div(
                        FormActions(
                            Submit('submit', 'Search')
                        ),
                    css_class='col-sm-2 col-md-2',
                    style='margin-top:25px;'
                    )
            )        
                        
                


