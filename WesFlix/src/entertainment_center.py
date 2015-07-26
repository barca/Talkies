from media import movie

description = ("This 1940 Kathrine Hepburn, romantic comedy focuses on a young "
 			   	"soccalite and her relationship between her ex-husband, fiance "
  			   	"and a reporter. Unclear about her feelings for all three men, "
  				"Tracy must decide whom she truly loves.")
poster_url = "http://bit.ly/1S3MYPB"
trailer_url = "https://www.youtube.com/embed/oCfuPPR7wnQ"
the_philadelphia_story = movie("The Philadelphia Story","July 18",
								poster_url, description, trailer_url,
								"","George Cukor", "112","Kathrine Hepburn",
								"Cary Grant")

desc = ("Matt Groening's critically acclaimed Sci-Fi cartoon is the "
 			  	"story of Philip J. Fry, cryogenically frozen "
 			 	"for 1000 years after pizza delivery gone wrong. He awakens "
 			 	"to find a world of alcholic robots, cyclopses, and mad "
 			 	"scientists. Join his adventures aboard the planet express ship!.")
trailer_url = "https://www.youtube.com/embed/-NeQ6aGWX74"
poster_url = "http://bit.ly/1CZ0u0c"
big_pic = "../static/imgs/futurama.png"

futurama = movie("Futurama","July 19", poster_url,
				desc, trailer_url, big_pic,
				"Peter Avanzino","89", "Billy West",
				"Katey Segal" )

description = ("Andy Dufresne (Tim Robbins) is sentenced to two consecutive "
		  "life terms in prison for the murders of his wife and her lover "
		  "and is sentenced to a tough prison.  However, only Andy knows "
 		  "he didn't commit the crimes.")
poster_url = "http://bit.ly/1I2Ag9I"
trailer_url = "https://www.youtube.com/embed/6hB3S9bIaco"
big_pic = "../static/imgs/shawshank.jpg"

shawshank_redemption = movie("Shawshank Redemption","July 20", poster_url,
						description, trailer_url, big_pic,
						"Frank Darabont", "142",
						"Tim Robbins", "Morgan Freedman")

description = ("the park is open. However, disaster strikes again, "
				"and the park plunges into chaos. Claire Dearing "
				"and Owen Grady are forced from safety in order "
				"to search for something dear to them")
trailer_url = "https://www.youtube.com/embed/RFinNxS5KN4"
poster_url = "http://bit.ly/1RwBPmJ"
big_pic = "../static/imgs/jWorld.jpg"

jurrassic_world = movie("Jurrassic World", "July 21", poster_url,
						description, trailer_url,big_pic, "Colin Trevorrow",
						"125", "Chris Pratt","Bryce Dallas")


desc = "This is the story of two killers, Harry Callahan and a serial killer."
trailer_url = "https://www.youtube.com/embed/HjBNldYiUmg"
poster_url = "http://bit.ly/1JnBErN"
big_pic = ""

dirty_harry = movie("Dirty Harry","July 22", poster_url,
					desc,trailer_url, big_pic, "Don Siegel", "103",
					"Clint Eastwood", "Andrew Robbinson")



description = ("Beginning in 2005, Palestinian Emad Burnet records his "
				"village's resistance to the encroachment of Israeli "
				"settlements. The title refers to the five cameras destroyed "
				"during the filmaking process")
poster_url = "../static/imgs/fiveCameras.jpg"
trailer_url = "https://www.youtube.com/embed/XID_UuxiGxM"

five_broken_cameras = movie("Five Broken Cameras",
						"July 22", poster_url, description, trailer_url,
						big_pic, "Ehmad Burnat", "94", "Ehmad Bernat",
						"Soraya Burnat")
description = ("There is a secret at a Catholic school, a nun, Merryl "
				"Streep is determined to find the truth "
				"even if those around her attempt to prevent her search. ")
poster_url = "http://bit.ly/1Ms5CvP"
trailer_url = "https://www.youtube.com/embed/Ad8gw-Qdjj8"

doubt = movie("Doubt","July 23", poster_url, description, trailer_url,
				big_pic, "John Shanley", "104", "Merryl Streep",
				"Phillip Seymour Hoffman")


description = ("Harrison Ford, Replicant Hunter. His assignment: eliminate "
				"four escaped Replicants from the colonies who "
				"have returned to Earth")

poster_url = "../static/imgs/bladerunner.jpg"
trailer_url = "https://www.youtube.com/embed/vFNUFqHyGZU"
blade_runner = movie("Blade Runner", "July 24", poster_url, description,
	trailer_url, big_pic, "Ridley Scott", "117", "Harrison Ford", "Sean Young" )



Movies = [the_philadelphia_story,futurama,shawshank_redemption,jurrassic_world,dirty_harry,five_broken_cameras,doubt,blade_runner]

dirty_harry_list = [dirty_harry]
