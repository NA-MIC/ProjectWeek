## Videos not working correctly?

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

2. Links to externally hosted videos (such as YouTube) will need an iframe. You can copy the correct iframe embedding code from the video, page itself, by clicking the Share button and then Embed

    Replace:

    ```
    https://youtu.be/ZWxE5QcGvE8
    ```

    with

    ````html
    <iframe width="420" height="315" src="https://www.youtube.com/embed/ZWxE5QcGvE8">
    </iframe>
    ````

## Images look squashed?

Edit the `img` tag for the image to have `width=800` and remove the height attribute
