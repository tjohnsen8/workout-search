from flask_table import Table, Col


class WorkoutResults(Table):
	date = Col('date')
	title = Col('Title')
	description = Col('Description')
	best_result = Col('Best Result') # use display
	notes = Col('Notes')
	rx = Col('Rx or Scaled')
	was_pr = Col('Hit a PR')


class Workout(object):
	def __init__(self, results_dic):
		self.date = results_dic['date']
		self.title = results_dic['title']
		self.description = results_dic['description']
		self.best_result = results_dic['best_result_display']
		self.notes = results_dic['notes']
		self.rx = results_dic['rx_or_scaled']
		self.was_pr = results_dic['pr']
