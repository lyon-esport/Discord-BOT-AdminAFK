translation:
	pybabel extract -o locale/messages.pot bdd config extensions functions locale main.py

update: translation
	pybabel update -i locale/messages.pot -d locale -l fr_FR

compile: 
	pybabel compile -d locale
