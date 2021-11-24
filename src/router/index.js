import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '@/views/Home'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import MyPage from '@/views/accounts/MyPage'
import MovieList from '@/views/movies/MovieList'
import MovieItem from '@/components/movies/MovieItem'
import Recommend from '@/views/recommend/Recommend'
// import ReviewList from '@/components/reviews/ReviewList'
import Reviews from '@/views/reviews/Reviews'
import ReviewItem from '@/components/reviews/ReviewItem'
import ReviewDetail from '@/components/reviews/ReviewDetail'
// import ReviewCreate from '@/components/community/ReviewCreate'
import Community from '@/views/community/Community'
import ArticleList from '@/components/community/ArticleList'
import ArticleDetail from '@/components/community/ArticleDetail'
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
    path: '/accounts/MyPage',
    name: 'MyPage',
    component: MyPage,
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
    props: true
  },  
  {
    path: '/reviews/item',
    name: 'ReviewItem',
    component: ReviewItem,
  },
  {
    path: 'reviews/reviewdetail/:id',
    name: 'ReviewDetail',
    component: ReviewDetail,
    props:true
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
    path: '/community/articles/articledetail/:id',
    name: 'ArticleDetail',
    component: ArticleDetail,
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
