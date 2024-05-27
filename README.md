## Flask Application Design for Displaying Recent News Articles

### HTML Files

- `index.html`:
   - This is the main HTML file that will display the recent news articles.
   - It should contain the necessary HTML structure to display the articles, such as a header, a container for the articles, and a footer.
   - It should also include the necessary HTML elements for styling and interactivity.

### Routes

- `/`:
   - This route will handle the rendering of the `index.html` file, which will display the recent news articles.
   - The route function should query the news API and store the results in a variable.
   - The variable can then be passed to the `index.html` file using the `render_template` function.