import { createRouter, createWebHistory } from 'vue-router'
import HomeShow from '../views/HomeShow.vue'
import Home from '../views/Home.vue'
import Movies from '../views/Movies.vue'
import MovieDetail from '../views/MovieDetail.vue'
import UserRecommend from '../views/UserRecommend.vue'
import ItemRecommend from '../views/ItemRecommend.vue'
import Stats from '../views/Stats.vue'

const routes = [
  { path: '/', component: HomeShow },
  { path: '/home-old', component: Home },
  { path: '/movies', component: Movies },
  { path: '/movies/:id', component: MovieDetail },
  { path: '/user-recommend', component: UserRecommend },
  { path: '/recommend/:movie_id', component: ItemRecommend },
  { path: '/stats', component: Stats }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router