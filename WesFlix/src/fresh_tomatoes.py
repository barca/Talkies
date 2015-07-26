import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<head>
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
'''


# The main page layout and title bar
main_page_content = '''
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
                <li class="active"><a href="#">Home</a></li>
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
    <div id="myCarousel" class="carousel slide" data-ride="carousel">
      <!-- Indicators -->
      <ol class="carousel-indicators">
        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
        <li data-target="#myCarousel" data-slide-to="1"></li>
        <li data-target="#myCarousel" data-slide-to="2"></li>
        <li data-target="#myCarousel" data-slide-to="3"></li>
      </ol>
      <div class="carousel-inner" role="listbox">
'''


# A single movie entry html template

carousel_finished = '''
    <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
        <span class="sr-only">Previous</span>
      </a>
      <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
        <span class="sr-only">Next</span>
      </a>
    </div>
    </div>

'''

carousel_template = '''
        <div class="{is_active}" id="{item_id}">
          <img class="first-slide img-responsive"src="{wide_pic}" alt="First slide">
          <div class="container">
            <div class="carousel-caption">
              <h1>{movie_title}</h1>
              <p>{movie_desc}</p>
              <p><a class="btn btn-lg btn-primary" href="{movie_title}.html" role="button">Watch Trailer</a></p>
            </div>
          </div>
        </div>

'''

sec_two = '''

    <div class="container marketing">
      <h2>Next Week's Movies: </h2>
      <!-- Three columns of text below the carousel -->
      <div class="row">
'''
sec_two_template = '''
        <div class="col-lg-3">
          <img src="{poster}" alt="poster" height="200">
          <h2>{movie_title}</h2>
          <p>{movie_desc}</p>
          <p><a class="btn btn-default" href="{movie_title}.html" role="button">View details &raquo;</a></p>
        </div><!-- /.col-lg-3 -->
'''

end_page = '''
    </div>
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
    <script src="../static/assets/js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>
'''


def set_carousel(movies):
    # The HTML content for this section of the page
    content = ''
    id = 1
    is_active = "item active"
    for movie in movies:
        # Extract the youtube ID from the url
        item_id = "item" + str(id)
        # Append the tile for the movie with its content filled in
        content += carousel_template.format(
            is_active = is_active,
            movie_title=movie.title,
            item_id=item_id,
            wide_pic=movie.big_pic,
            movie_desc=movie.desc,
        )
        id += 1
        is_active = "item"
    return (main_page_content + content + carousel_finished)

def set_next_week_lineup(movies):
# The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        # Append the tile for the movie with its content filled in
        content += sec_two_template.format(
            movie_title=movie.title,
            poster_name= movie.title,
            poster=movie.poster,
            movie_desc=movie.desc
        )
    return (sec_two + content + end_page)



def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = set_carousel(movies[:4]) + set_next_week_lineup(movies[4:])

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
