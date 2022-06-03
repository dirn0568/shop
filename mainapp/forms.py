from django import forms

class SearchReportForm(forms.Form):
    search_word = forms.CharField(label='Search Word',
                                  widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                'autocomplete': 'off',
                                                                'size': '40',
                                                                'style': 'font-size: large',
                                                                }))