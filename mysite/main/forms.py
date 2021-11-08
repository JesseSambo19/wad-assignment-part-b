from django import forms

class CreateNewList(forms.Form):
	name = forms.CharField(label="Name", max_length=200)
	check = forms.BooleanField(required=False)

class UpdateForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))

	class Meta:
		# model = task
		fields = ['title', 'due', 'complete']