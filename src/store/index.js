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
  },
  mutations: {
    GET_MOVIES(state, res) {
      state.movies = res
    },
    GET_REVIEWS(state, res) {
      state.reviews = res
    },
  },
  actions: {
    getMovies({commit}) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/`,
      })
      .then(res => {
        commit('GET_MOVIES', res.data)
        // commit('GET_MOVIE_TITLES', res.data)
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
        // commit('GET_MOVIE_TITLES', res.data)
      })
      .catch(err => console.log(err))
    },    
  },
  getters: {
    movies(state) {
      return state.movies
    },
    reviews(state) {
      return state.reviews
    }
  },
  modules: {
  }
})
