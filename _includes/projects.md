<!-- Begin _includes/projects.md -->

{% comment %}Extract event name (e.g "PW39_2023_Montreal"). {% endcomment %}
{% assign event_name = page.path | split: '/' | first %}

{% assign project_count = 0 %}
{% assign categories = "" %}
{% assign uncategorized = "" %}

{% for requested_category in page.project_categories %}
{% include project_generate_category.md %}
{% endfor %}

{% assign requested_category = "Uncategorized" %}
{% include project_generate_category.md %}

_The {{ event_name }} event has a total of {{ project_count }} projects._

{{ categories }}

### Uncategorized

{{ uncategorized }}

<!-- End _includes/projects.md -->
