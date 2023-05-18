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

_This section lists projects that either have no category assigned, are assigned to the "Uncategorized" category, or are assigned to a different category than the ones listed above. If you are unable to find a category that is suitable for your project, or believe that a specific category is missing, please discuss it with the [organizers](#organizers)._

{{ uncategorized }}

<!-- End _includes/projects.md -->
