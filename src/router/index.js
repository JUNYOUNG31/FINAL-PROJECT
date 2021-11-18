import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieList from '@/views/movies/MovieList'
import ReviewList from '@/views/community/ReviewList'
import ReviewDetail from '@/components/ReviewDetail'
import MovieDetail from '@/components/MovieDetail'
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
    path: '/community/reviewdetail',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path: '/movies/moviedetail',
    name: 'MovieDetail',
    component: MovieDetail,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
