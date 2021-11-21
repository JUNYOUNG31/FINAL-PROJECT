import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieList from '@/views/movies/MovieList'
import Community from '@/views/community/Community'
import MovieItem from '@/components/MovieItem'
import ReviewList from '@/components/community/ReviewList'
import ReviewItem from '@/components/community/ReviewItem'
import ReviewCreate from '@/components/community/ReviewCreate'

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
    path: '/movies/movieitem',
    name: 'MovieItem',
    component: MovieItem,
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },  
  {
    path: '/community',
    name: 'ReviewItem',
    component: ReviewItem,
  },  
  {
    path: '/community',
    name: 'ReviewList',
    component: ReviewList,
  },
  {
    path: '/community',
    name: 'ReviewCreate', 
    component: ReviewCreate,
  },  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
