import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '@/views/Home'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MovieList from '@/views/movies/MovieList'
import MovieItem from '@/components/movies/MovieItem'
import Reviews from '@/views/reviews/Reviews'
// import ReviewList from '@/components/reviews/ReviewList'
import Community from '@/views/community/Community'
import ArticleList from '@/components/community/ArticleList'
import Recommend from '@/views/recommend/Recommend'
import Profile from '@/views/accounts/Profile'
import ReviewItem from '@/components/reviews/ReviewItem'
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

  // accounts
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
    props: true,
  },

  // movies
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

  // reviews
  {
    path: '/reviews',
    name: 'Reviews',
    component: Reviews,
  },  
  {
    path: '/reviews/item',
    name: 'ReviewItem',
    component: ReviewItem,
  },
  // {
  //   path: '/community',
  //   name: 'ReviewCreate', 
  //   component: ReviewCreate,
  // },  
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/community/articles',
    name: 'ArticleList',
    component: ArticleList,
    props: true
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
