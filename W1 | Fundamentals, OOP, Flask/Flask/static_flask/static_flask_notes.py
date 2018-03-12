Static content is any content that can be served up to the client without being modified, generated, or processed by the server. Every framework will have its own way of serving static content. Flask serves static content from a directory called static.. Much like our templates directory, the static directory must be called static. This static folder will be used to serve all of your stylesheets, images, and JavaScript files.

Now, say we placed a CSS file, a JavaScript file, and an image directly into our static folder. We can then access them in our HTML templates, like so:

<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='my_style_sheet.css') }}">
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='my_script.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='my_img.png') }}">


Note: although Flask knows to look for static files in the static directory, we must tell it when and where to do so, as shown above.

Organization
It is common to create a few more folders to organize our static files into categories according to document type. We can call them css, js, and img and house the corresponding files in the different folders. We can reflect these changes in our previous tags with the following changes in the href/src attributes. Notice the way we change the file name in the url_for function:

<!-- linking a css style sheet -->
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/my_style_sheet.css') }}">
<!-- linking a javascript file -->
<script type="text/javascript" src="{{ url_for('static', filename='js/my_script.js') }}"></script>
<!-- linking an image -->
<img src="{{ url_for('static', filename='img/my_img.png') }}">

All static content must go inside of the static folder
The folder must be named static
