{
	// Place your snippets for python here. Each snippet is defined under a snippet name and has a prefix, body and 
	// description. The prefix is what is used to trigger the snippet and the body will be expanded and inserted. Possible variables are:
	// $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders. Placeholders with the 
	// same ids are connected.
	// Example:
	// "Print to console": {
	// 	"prefix": "log",
	// 	"body": [
	// 		"console.log('$1');",
	// 		"$2"
	// 	],
	// 	"description": "Log output to console"
	// }
	"django_app_urls": {
		"prefix": "djau",
		"body": [
			"from django.urls import path",
			"from .views import $1",
			"",
			"urlpatterns = [",
			"    path('$2', $1.as_view(), name='$3')",
			"]",
			""
		],
		"description": "django_app_urls"
	},
	"Django Url Patterns - CRUD": {
		"prefix": "djuc",
		"body": [
			"from django.urls import path",
			"from .views import $1ListView, $1DetailView, $1CreateView, $1UpdateView, $1DeleteView",
			"",
			"urlpatterns = [",
			"    path('', $1ListView.as_view(), name='$2_list'),",
			"    path('<int:pk>/', $1DetailView.as_view(), name='$2_detail'),",
			"    path('create/', $1CreateView.as_view(), name='$2_create'),",
			"    path('<int:pk>/update/', $1UpdateView.as_view(), name='$2_update'),",
			"    path('<int:pk>/delete/', $1DeleteView.as_view(), name='$2_delete'),",
			"]"
		],
		"description": "Django Url Patterns - CRUD"
	},
	"Django Views - CRUD": {
		"prefix": "djvc",
		"body": [
			"from django.views.generic import (",
			"    ListView,",
			"    DetailView,",
			"    CreateView,",
			"    UpdateView,",
			"    DeleteView,",
			")",
			"from django.urls import reverse_lazy",
			"from .models import $1",
			"",
			"",
			"class $1ListView(ListView):",
			"    template_name = \"$2/$3-list.html\"",
			"    model = $1",
			"",
			"",
			"class $1DetailView(DetailView):",
			"    template_name = \"$2/$3-detail.html\"",
			"    model = $1",
			"",
			"",
			"class $1CreateView(CreateView):",
			"    template_name = \"$2/$3-create.html\"",
			"    model = $1",
			"    fields = []",
			"",
			"",
			"class $1UpdateView(UpdateView):",
			"    template_name = \"$2/$3-update.html\"",
			"    model = $1",
			"    fields = []",
			"",
			"",
			"class $1DeleteView(DeleteView):",
			"    template_name = \"$2/$3-delete.html\"",
			"    model = $1",
			"    success_url = reverse_lazy(\"$3_list\")"
		],
		"description": "Django Views - CRUD"
	},
}