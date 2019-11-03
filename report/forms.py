from django import forms


class AsyncResultForgetForm(forms.Form):
    async_result = forms.CharField(label='AsyncResult', max_length=100)
