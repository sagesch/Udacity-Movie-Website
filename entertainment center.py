import fresh_tomatoes
import media


# movie info, like thier titles and storyline.
                          # Title            Storyline                                                                            Postor image                                                                      Embeded youtube link
terminator = media.Movie("The Terminator", "A robot played as Arnold Swarchenagger goes back in time to try and kill someone.", "https://upload.wikimedia.org/wikipedia/en/7/70/Terminator1984movieposter.jpg", "https://www.youtube.com/watch?v=k64P4l2Wmeg")

sneakers = media.Movie("Sneakers", "A group of people who specilize in finding flaws in security systems are hired to steal a black box.", "https://upload.wikimedia.org/wikipedia/en/a/aa/Sneakersmovie.jpg", "https://www.youtube.com/watch?v=G_XRqJV2zdk")

#groups the movies into one single variable
movies = [terminator,sneakers]

#oopens fresh_tomatoes.py, which then creates and opens the webpage.
fresh_tomatoes.open_movies_page(movies)
