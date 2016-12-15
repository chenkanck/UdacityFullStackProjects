import media
import fresh_tomato

toy_story = media.Movie(
	"Toy Story",
	"A toy story of a boy and his toys",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4"
	)

avatar = media.Movie(
	"Avatar",
	"A marine on an alien planet",
	"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=-9ceBgWV8io"
	)

star_wars_the_force_awakens = media.Movie(
	"Star Wars: The Force Awakens",
	"Approximately 30 years after the destruction of the second Death Star, "
	"the last remaining Jedi, Luke Skywalker, has disappeared. ",
	"https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg", #NOQA
	"https://www.youtube.com/watch?v=sGbxmsDFVnE"
	)

movies = [toy_story, avatar, star_wars_the_force_awakens]
fresh_tomato.open_movies_page(movies)
