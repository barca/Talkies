import webbrowser
import os
import re


# Styles and scripting for the page
main_page_start = '''

<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>WesFlix</title>

    <!-- Bootstrap core CSS -->
    <link href="../static/lib/bootstrap.min.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="../static/assets/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->

    <!-- Custom styles for this template -->
    <link href="../static/css/carousel.css" rel="stylesheet">
    <link href="../static/css/styles.css" rel="stylesheet">
  </head>
<!-- NAVBAR
================================================== -->
 <body>
    <div class="navbar-wrapper">
      <div class="container">

        <nav class="navbar navbar-inverse navbar-static-top">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="#">WesFlix</a>
            </div>
            <div id="navbar" class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li><a href="index.html">Home</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li class="active"><a href="calendar.html">Calendar</a></li>
              </ul>
            <div class="input-group" style="padding-top: 8px">
              <input type="text" class="form-control" id="input" placeholder="Search for a specific trailer...">
              <span class="input-group-btn">
                <button class="btn btn-default" type="button" id="input">Go! </button>
              </span>
            </div>
          </div>
        </nav>
      </div>
    </div>

    <hr class="featurette-divider" style="border-top-color: #fff">
    <div class="container">


'''


content_template = '''
    <div class="row featurette">
      <div class="col-md-2"><h2>{movie_title}</h2>
        <h2 style="margin-top:0px">{movie_date}</h2>
        </div>
        <div class="col-md-8"><p class="text-center calendar-item">{movie_desc}</p>
        </div>
        <div class="col-md-2"><p><a class="btn btn-default calendar-item" href="{movie_title}.html" role="button">View details &raquo;</a></p></div>
      </div>
      <hr class="featurette-divider calendar-divider">
'''

end_page = '''
      <!-- FOOTER -->
      <footer>
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2015 Tyler Harden. </p>
      </footer>

    </div><!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="../static/lib/jquery.min.js"></script>
    <script src="../static/lib/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="../static/assets/js/vendor/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../stati/assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>

'''


def set_contents(movies):
    content = ""
    for movie in movies:
      content += content_template.format(
          movie_title=movie.title,
          movie_date=movie.date,
          movie_desc=movie.desc
      )
    return (main_page_start + content + end_page)


def write_calendar(movies):
    # Create or overwrite the output file

    # Replace the movie tiles placeholder generated content
    output_file = open('calendar.html', 'w')
    # Write a file for each page
    output_file.write(set_contents(movies))
    output_file.close()