import webbrowser
import os
import re


# Styles and scripting for the page
main_page_start = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../../favicon.ico">

    <title>WesFlix</title>

    <link href="../static/lib/bootstrap.min.css" rel="stylesheet">
    <script src="../static/assets/js/ie-emulation-modes-warning.js"></script>
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
                <li><a href="calendar.html">Calendar</a></li>
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

'''


content_template = '''
   <div class="row featurette">
      <div class="container" style="padding-left:0;">
        <div class="col-md-4" id="infoSec">
          <img src="{movie_poster}" alt="Movie Poster"  height="300">
          <h2>10:00 PM, {movie_date}</h2>
          <h2>{movie_title}</h2>
        </div>
        <div class="col-md-8">
          <iframe class="embed-responsive-item" width="700" height="394" src="{trailer_url}" frameborder="0" allowfullscreen></iframe>
          <div class="row featurette">
            <div class="col-md-2">
            <h2>Director:</h2>
            <h2>Runtime:</h2>
            </div>
            <div class="col-md-4">
            <h2 class="text-muted">{movie_director}</h2>
            <h2 class="text-muted">{movie_runtime} minutes</h2>
            </div>
            <div class="col-md-1">
            <h2>Cast:</h2>
            </div>
            <div class="col-md-5">
            <h2 class="text-muted">{lead_actor}</h2>
            <h2 class="text-muted">{second_actor}</h2>
            </div>
          </div>
        </div>
      </div>
       <div class="container">
        <h2> About: </h2>
        <p>{movie_desc}
        </p>
     </div>
'''

end_page = '''
      <hr class="featurette-divider min" style="border-top-color: #fff">
      <!-- FOOTER -->
      <footer>
        <div class="container">
        <p class="pull-right"><a href="#">Back to top</a></p>
        <p>&copy; 2015 Tyler Harden. </p>
        </div>
      </footer>

    <!-- /.container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="../static/lib/jquery.min.js"></script>
    <script src="../static/lib/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="../static/assets/js/vendor/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../static/assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
'''


def set_contents(movie):
    content = content_template.format(
        movie_title=movie.title,
        movie_date=movie.date,
        movie_director=movie.director,
        movie_runtime=movie.runtime,
        trailer_url=movie.trailer,
        lead_actor=movie.main_cast_member,
        second_actor=movie.secondary_cast_member,
        movie_poster=movie.poster,
        movie_desc=movie.desc
    )
    return (main_page_start + content + end_page)


def write_detailed_pages(movies):
    # Create or overwrite the output file

    # Replace the movie tiles placeholder generated content
    for each in movies:
      file_name = each.title + '.html'
      output_file = open(file_name, 'w')
      # Write a file for each page
      output_file.write(set_contents(each))
      output_file.close()
