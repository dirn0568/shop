from django import forms

class SearchReportForm(forms.Form):
    search_word = forms.CharField(label='아이디 검색',
                                  widget=forms.TextInput(attrs={'autofocus': 'autofocus',
                                                                'autocomplete': 'off',
                                                                'size': '40',
                                                                'style': 'font-size: large',
                                                                }))