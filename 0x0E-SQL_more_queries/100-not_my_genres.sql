-- Lists all genres of the database hbtn_0d_tvshows
-- not linked to the show Dexter.
-- Records are sorted by ascending genre name.
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN (
  SELECT tv_genres.name
  FROM tv_shows
  JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
  WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
