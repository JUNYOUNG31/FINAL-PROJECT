import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
// import router from '@/router'

const SERVER_URL = 'http://127.0.0.1:8000/'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: []
  },
  mutations: {
    GET_MOVIES(state, res) {
      state.movies = res
    },
  },
  actions: {
    getMovies({commit}, token) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/`,
        headers: token,
      })
      .then(res => {
        commit('GET_MOVIES', res.data)
        // commit('GET_MOVIE_TITLES', res.data)
      })
      .catch(err => console.log(err))
    },
  },
  getters: {
    movies(state) {
      return state.movies
    }
  },
  modules: {
  }
})
