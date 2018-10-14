import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        " http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=azyK_k52R1w")
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://media.comicbook.com/2015/12/avatarsequels-162567.png ",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8 ")

#print (avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg ",
                             " https://www.youtube.com/watch?v=oP7kExN8LFA")

ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg ",
                          " https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                " http://jaquo.com/wp-content/uploads/2015/09/maxresdefault.jpg",
                                " https://www.youtube.com/watch?v=BYRWfS2s2v4")


hunger_games = media.Movie("Hunger games",
                                "A really real reality show",
                                "http://t2.gstatic.com/images?q=tbn:ANd9GcS58mYVyiI3LTihImFjn6QBLU_mcHXZP3LaGoWN9u5bzuvW3lvC ",
                                " https://www.youtube.com/watch?v=n-7K_OjsDCQ")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
print (media.Movie.__name__)
