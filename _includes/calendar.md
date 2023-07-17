<!-- Begin _includes/calendar.md -->

{% raw %}
<!--
This template expects the following parameters:
* "from" formatted as ISO 8601
* "to" formatted as ISO 8601

Example:
{% include calendar.md from="2023-06-12" to="2023-06-16" %}

References:
* https://jekyllrb.com/docs/includes/#passing-parameters-to-includes
* https://shopify.github.io/liquid/filters/date/
-->
{% endraw %}

<div id="calendar-container">
</div>

<!--
Adapted from https://stackoverflow.com/questions/31821974/support-user-time-zone-in-embedded-google-calendar
-->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jstimezonedetect/1.0.7/jstz.min.js" integrity="sha512-pZ0i46J1zsMwPd2NQZ4IaL427jXE2RVHMk3uv/wPTNlBVp9AbB1L65/4YdrXRPLEmyZCkY9qYOOsQp44V4orHg==" crossorigin="anonymous"></script>

<script type="text/javascript">
  var timezone = jstz.determine();
  var iframe_src = 'https://calendar.google.com/calendar/embed?src=kitware.com_sb07i171olac9aavh46ir495c4%40group.calendar.google.com&mode=WEEK&dates={{ include.from | date: "%Y%m%d" }}%2f{{ include.to  | date: "%Y%m%d" }}&ctz=' + timezone.name()
  var iframe_html = '<iframe src="' + iframe_src + 'style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>'
  document.getElementById('calendar-container').innerHTML = iframe_html;
</script>

[How to add this calendar to your own?](../common/Calendar.md)

<!-- End _includes/calendar.md -->
