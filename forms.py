from wtforms import Form, StringField, SelectField

class WorkoutSearchForm(Form):
	search = StringField('')