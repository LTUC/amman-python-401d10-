{
	"Django Template Block": {
		"prefix": "dtb",
		"body": [
			"{% block $1 %}",
			"",
			"{% endblock $1 %}"
		],
		"description": "Django Template Block"
	},
	"Django Template Extends": {
		"prefix": "dte",
		"body": [
			"{% extends '$1.html' %}"
		],
		"description": "Django Template Extends"
	},
	"Django Template Tag": {
		"prefix": "dtt",
		"body": [
			"{% $1 %}"
		],
		"description": "Django Template Tag"
	},
	"django template child": {
		"prefix": "dtc",
		"body": [
			"{% extends '$1.html' %}",
			"",
			"{% block content %}",
			"  <h2>$2 coming soon</h2>",
			"{% endblock content %}"
		],
		"description": "django template child"
	},
	"Django Template Form": {
		"prefix": "dtf",
		"body": [
			"<form action=\"\" method=\"POST\">",
			"  {% csrf_token %}",
			"  {{ form.as_p }}",
			"  <input type=\"submit\" value=\"$1\">",
			"</form>"
		],
		"description": "Django Template Form"
	}
}