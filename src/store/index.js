import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import router from '@/router'

const SERVER_URL = 'http://127.0.0.1:8000/'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    reviews: [],
    movieTitles: []
  },
  mutations: {
    GET_MOVIES(state, res) {
      state.movies = res
    },
    GET_REVIEWS(state, res) {
      state.reviews = res
    },
    CREATE_REVIEWS(state, res) {
      state.reviews = res
    },
    GET_MOVIE_TITLES(state, res) {
      const tmp_list = []
      for (var value of res) {
        const tmp = {
          name: value.title, value: value.title
        }
        tmp_list.push(tmp)
      }
      state.movieTitles = tmp_list
    }
  },
  actions: {
    getMovies({commit}) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/`,
      })
      .then(res => {
        commit('GET_MOVIES', res.data)
        commit('GET_MOVIE_TITLES', res.data)
      })
      .catch(err => console.log(err))
    },
    getReviews({commit}) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/community/`,
      })
      .then(res => {
        commit('GET_REVIEWS', res.data)   
      })
      .catch(err => console.log(err))
    },    
    createReview({commit}, reviewcreate) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}movies/community/create/`,
        data: reviewcreate.reviewItem,
        headers: reviewcreate.token
      })
      .then(res => {
        console.log(reviewcreate)
        commit('CREATE_REVIEWS', res.data)       
      })
      .catch(err => {
        console.log(err)
        console.log(reviewcreate)
      })
    },    
  },
  getters: {
    movies(state) {
      return state.movies
    },
    reviews(state) {
      return state.reviews
    },
    movieTitles(state) {
      return state.movieTitles
    },
  },
  modules: {
  }
})
