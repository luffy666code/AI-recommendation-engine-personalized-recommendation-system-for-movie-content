import http from './http'

export const getMovies = (params = {}) => http.get('/movies', { params })
export const getMovie = (id) => http.get(`/movies/${id}`)
export const postRating = (payload) => http.post('/ratings', payload)
export const getUserRatings = (user_id) => http.get(`/ratings/user/${user_id}`)
export const getUserRecommend = (user_id, top_n = 10) => http.get(`/recommend/user/${user_id}?top_n=${top_n}`)
export const getItemRecommend = (movie_id, top_n = 10) => http.get(`/recommend/item-based/${movie_id}?top_n=${top_n}`)

export default http