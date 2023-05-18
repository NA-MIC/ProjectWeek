<!-- Begin _includes/projects.md -->

{% comment %}Extract event name (e.g "PW39_2023_Montreal"). {% endcomment %}
{% assign event_name = page.path | split: '/' | first %}

{% assign project_count = 0 %}
{% assign categories = "" %}
{% assign uncategorized = "" %}

{% for pw_page in site.pages %}

  {% comment %}Extract page event name (e.g "PW39_2023_Montreal"){% endcomment %}
  {% assign pw_page_event_name = pw_page.path | split: '/' | first %}

  {% comment %}Only process page associated with the current event.{% endcomment %}
  {% if pw_page_event_name != event_name %}
    {% continue %}
  {% endif %}

  {% comment %}Extract page event type (e.g "Projects").{% endcomment %}
  {% assign pw_page_type = pw_page.path | split: '/' | slice: 1 | first %}

  {% comment %}Only process pages located in the "Projects" directory.{% endcomment %}
  {% if pw_page_type != "Projects" %}
    {% continue %}
  {% endif %}

  {% comment %}Extract page project name (e.g "SlicerVRInteraction").{% endcomment %}
  {% assign project_name = pw_page.path | split: '/' | slice: 2 | first | downcase %}

  {% comment %}Ignore "Template" and "README.md" file.{% endcomment %}
  {% if project_name == "template" or project_name == "readme.md" %}
    {% continue %}
  {% endif %}

  {% assign project_count = project_count | plus: 1 %}

  {% assign pw_page_category = pw_page.category | default:"Uncategorized" %}

  {% if page.project_categories contains pw_page_category %}

    {% comment %}If if applies, add catergory header.{% endcomment %}
    {% unless categories contains pw_page_category %}
{% capture categories %}
{{ categories }}
### {{ pw_page_category }}
{% endcapture %}
      {% endunless %}

    {% comment %}Append category entry.{% endcomment %}
{% capture categories %}
{{ categories }}
1. [{{ pw_page.project_title }}]({{ pw_page.url }}) (
{%- for investigator in pw_page.key_investigators -%}
    {{ investigator.firstname }} {{ investigator.lastname }}{% unless forloop.last %}, {% endunless -%}
{%- endfor -%}
)
{% endcapture %}

  {% else %}

{% capture uncategorized %}
{{ uncategorized }}
1. [{{ pw_page.project_title }}]({{ pw_page.url }}) (
{%- for investigator in pw_page.key_investigators -%}
    {{ investigator.firstname }} {{ investigator.lastname }}{% unless forloop.last %}, {% endunless -%}
{%- endfor -%}
)
{% endcapture %}

  {% endif %}
{% endfor %}

_The {{ event_name }} event has a total of {{ project_count }} projects._

{{ categories }}

### Uncategorized

{{ uncategorized }}

<!-- End _includes/projects.md -->
