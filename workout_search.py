import csv


def SugarWodSearch(query):
	results = []
	with open('data/workouts.csv', newline='', encoding='latin-1') as csvfile:
		workout_reader = csv.DictReader(csvfile)
		# now search for something
		for row in workout_reader:
			for col, entry in row.items():
				if query.lower() in entry.lower():
					results.append(row)
	return results


def test_search(query):
	results = SugarWodSearch(query)
	for result in results:
		print(result['title'] + ' ' + result['best_result_display'])


if __name__ == '__main__':
	test_search('Zercher')
