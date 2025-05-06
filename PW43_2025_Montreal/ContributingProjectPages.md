---
---
{% comment %}Extract event name (e.g "PW39_2023_Montreal"). {% endcomment %}
{%- assign event_name = page.path | split: '/' | first -%}

# Contributing Project Pages

## Creating new project pages

With the [Project Week GitHub Issue page](https://github.com/NA-MIC/ProjectWeek/issues/new/choose), you have two options to create your Project Page:


1. [Create a Project](https://github.com/NA-MIC/ProjectWeek/issues/new?assignees=sjh26&labels=project%2Cevent%3A{{ event_name }}&projects=&template=project.yml&title=Project%3A+) issue: If you are ready to create your page, you can simply create a “Project” issue. This issue will allow you to fill out a convenient form to provide the necessary details.  The Project Week website team will then review the issue and trigger the page creation pull request.

2. [Create the project page yourself using the template](Projects/README.md): If you prefer to create the Project Page yourself, you can still do so by using the provided template and submitting a pull request.

## Project Creation Tips

- Get your project pages created early!  The day before is best to make sure everything you need for you presentation is available.  The ProjectWeek site will be closed to edits for the ***10 minutes before*** both the opening and closing presentation session to ensure site generation. After this 10 minute period edits will be re-enabled.

- If you are [creating the project page yourself using the template](Projects/README.md), **don't reuse a project page template from a previous year.**  We have made significant updates to the template to support auto-generation of project pages, so previous years' templates will not function properly.

    - When naming the file, **please ensure there are no spaces/special characters in the folder or file name**
    - Make sure to fill out / update all of the information at the top of the README file (title, category, location, etc)

- Remember to fill out the title for your project when using the [project creation issue](https://github.com/NA-MIC/ProjectWeek/issues/new?assignees=drouin-simon%2Cpiiq%2Crafaelpalomar%2Csjh26%2Ctkapur&labels=project%2Cevent%3A{{ event_name }}&projects=&template=project.yml&title=Project%3A+)

- Check the formatting on the Key Investigators list when creating a [project issue](https://github.com/NA-MIC/ProjectWeek/issues/new?assignees=drouin-simon%2Cpiiq%2Crafaelpalomar%2Csjh26%2Ctkapur&labels=project%2Cevent%3A{{ event_name }}&projects=&template=project.yml&title=Project%3A+) (this is critical for page generation):

    `- Firstname Lastname (Affiliation, Country)`

## Updating existing project pages

Here are the steps using the GitHub web interface:

1. Navigate to your project's `README.md` on the GitHub website. For instance, if you want to update a project called **YourProjectName**, visit the URL like the following:

    ```
    https://github.com/NA-MIC/ProjectWeek/blob/master/{{ event_name }}/Projects/<b>YourProjectName</b>/README.md
    ```

2. Click the edit button, as shown in this screenshot: ![Screenshot 2023-06-12 10 43 35](https://github.com/NA-MIC/ProjectWeek/assets/25040869/ab01a7bf-c1e4-4c23-9aca-e2c6421ca530)

3. You can now edit the page, add images by dragging and dropping, and more.

4. Once done, click "Commit Changes", and follow the instructions to create a fork and a pull request to add your changes to the webpage. See this screenshot for reference: ![Screenshot 2023-06-12 10 50 50](https://github.com/NA-MIC/ProjectWeek/assets/25040869/180e81bb-d4f9-4f65-8569-a93192b2828e)

## Videos in project pages

Here are some steps to make sure all of your awesome videos render correctly:

1. Videos added by drag and drop will render correctly when viewed through GitHub, but need some extra tweaks to work in the final generated website.


    In your `README.md`, if you have a video link that looks like this:

    ```
    https://github.com/NA-MIC/ProjectWeek/assets/66890913/8f257f29-fa9c-4319-8c49-4138003eba27
    ```

    Update it to:

    ```html
    <video
      controls muted
      src="https://github.com/NA-MIC/ProjectWeek/assets/66890913/8f257f29-fa9c-4319-8c49-4138003eba27"
      style="max-height:640px; min-height: 200px">
    </video>
    ```

2. Links to externally hosted videos (such as YouTube) will need an iframe.

    Replace:

    ```
    https://youtu.be/ZWxE5QcGvE8
    ```

    with

    ````html
    <iframe width="420" height="315" src="https://www.youtube.com/embed/ZWxE5QcGvE8">
    </iframe>
    ````
