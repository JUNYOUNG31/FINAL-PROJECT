import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '@/views/Home'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieList from '@/views/movies/MovieList'
import Community from '@/views/community/Community'
import MovieItem from '@/components/movies/MovieItem'
import ReviewList from '@/components/community/ReviewList'
import Article from '@/views/articles/Article'
import Recommend from '@/views/recommend/Recommend'
import Profile from '@/views/accounts/Profile'
// import ReviewItem from '@/components/community/ReviewItem'
// import ReviewCreate from '@/components/community/ReviewCreate'

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(() => {
        return window.location.reload()
    })
};
 

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/home',
  //   name: 'Home',
  //   component: Home,
  // },
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
    path: '/accounts/Profile',
    name: 'Profile',
    component: Profile,
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
  // {
  //   path: '/community',
  //   name: 'ReviewItem',
  //   component: ReviewItem,
  // },  
  {
    path: '/community/list',
    name: 'ReviewList',
    component: ReviewList,
  },
  // {
  //   path: '/community',
  //   name: 'ReviewCreate', 
  //   component: ReviewCreate,
  // },  
  {
    path: '/articles',
    name: 'Article',
    component: Article,
  },
  {
    path: '/recommend',
    name: 'Recommend',
    component: Recommend,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
