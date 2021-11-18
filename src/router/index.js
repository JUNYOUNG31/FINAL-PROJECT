import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieList from '@/views/movies/MovieList'
import ReviewList from '@/views/community/ReviewList'
import MovieItem from '@/components/MovieItem'
import ReviewItem from '@/components/ReviewItem'
Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/movies/movielist',
    name: 'MovieList',
    component: MovieList,
  },
  {
    path: '/community/reviewList',
    name: 'ReviewList',
    component: ReviewList,
  },
  {
    path: '/movies/movieitem',
    name: 'MovieItem',
    component: MovieItem,
  },
  {
    path: '/community/reviewitem',
    name: 'ReviewItem',
    component: ReviewItem,
  },  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
