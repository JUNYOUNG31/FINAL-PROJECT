import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import vueMoment from 'vue-moment'
// import createPersistedState from "vuex-persistedstate"; 

const SERVER_URL = 'http://127.0.0.1:8000/'
Vue.use(Vuex)
Vue.use(vueMoment)

export default new Vuex.Store({
  plugins: [],
  state: {
    movies: [],
    reviews: [],
    movieTitles: [],
    comments: [],
    comment: null,
  },
  mutations: {
    GET_MOVIES(state, res) {
      state.movies = res
    },
    GET_REVIEWS(state, res) {
      state.reviews = res
    },
    CREATE_REVIEW(state, res) {
      state.reviews = res      
    },
    UPDATE_REVIEW(state, reviewItem) {
      state.reviews = state.reviews.map((review) => {
        if (review === reviewItem) {
          return { ...review,
            title: reviewItem.title,
            content: reviewItem.content,
            rank: reviewItem.rank,
          }
        }  
        return review
      })    
    },
    DELETE_REVIEW(state, reviewItem) {
      const index = state.reviews.indexOf(reviewItem)
      state.reviews.splice(index, 1)
    },
    
    CREATE_COMMENT(state, res) {
      state.comments.push(res)
    },
    READ_COMMENT(state, res) {
      state.comment = res
    },
    UPDATE_COMMENT(state, commentItem) {
      state.comments = state.comments.map((comment) => {
        if (comment === commentItem) {
          return { ...comment, content: commentItem.content }
        }
        return comment
      })
    },
    DELETE_COMMENT(state, commentItem) {
      const index = state.comments.indexOf(commentItem)
      state.comments.splice(index, 1)
    },
    GET_COMMENTS(state, res) {
      state.comments = res
    },

    GET_MOVIE_TITLES(state, res) {
      const tmp_list = []
      for (var value of res) {
        const tmp = {
          name: value.title, value: value, id: value.pk
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
      .catch(err => {
        console.log(err)        
      })
    },    
    createReview({commit}, reviewcreate) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}movies/community/create/`,
        data: reviewcreate.reviewItem,
        headers: reviewcreate.token
      })
      .then(res => {       
        console.log(res)
        commit('CREATE_REVIEW', res.data) 
        router.push({name:'Community'})
        router.go()       
      })
      .catch( err => {
        console.log(err)        
      })
    },
    updateReview({commit}, updateItem) {
      axios({
        method: 'PUT',
        url: `${SERVER_URL}movies/community/${updateItem.review_id}/`,    
        data: updateItem.reviewItem,
        headers: updateItem.token
      }) 
      .then(res => {       
        console.log(res)
        commit('UPDATE_REVIEW')               
      })
    },
    deleteReview({commit}, deleteItem) {
      axios({
        method: 'PUT',
        url: `${SERVER_URL}movies/community/${deleteItem.review_id}/`,
        headers: deleteItem.token
      }) 
      .then(res => {       
        console.log(res)
        commit('DELETE_REVIEW')   
        router.go()            
      })
    },





    // COMMUNITY - COMMENT ACTIONS
    getComments({commit}, objs) {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/community/${objs.review_id}/comment_create/`,
        headers: objs.token
      })
      .then((res) => {
        commit('GET_COMMENTS', res.data)
      })
      .catch(err => console.log(err))
    },
    createComment({commit}, objs) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}movies/community/${objs.review_id}/comment_create/`,
        data: objs.commentItem,
        headers: objs.token
      })
      .then((res) => {
        commit('CREATE_COMMENT', res.data)
      })
      .catch(err => console.log(err))
    },
    // readComment({commit}, objs) {
    //   axios({
    //     method: 'GET',
    //     url: `${SERVER_URL}community/comments/${objs.comment_id}/`,
    //     headers: objs.token
    //   })
    //   .then((res) => {
    //     commit('READ_COMMENT', res.data)
    //   })
    //   .catch(err => console.log(err))
    // },
    updateComment({commit}, objs) {
      axios({
        method: 'PUT',
        url: `${SERVER_URL}movies/community/${objs.review_id}/${objs.comment_id}/`,
        data: objs.commentItem,
        headers: objs.token
      })
      .then((res) => {
        commit('UPDATE_COMMENT', res.data)
        router.push({name:'Community'})
      })
      .catch(err => console.log(err))
    },
    deleteComment({commit}, objs) {
      axios({
        method: 'DELETE',
        url: `${SERVER_URL}movies/community/${objs.review_id}/${objs.comment_id}/`,
        headers: objs.token
      })
      .then((res) => {
        commit('DELETE_COMMENT', res.data)
        router.push({name:'Community'})
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
    },
    movieTitles(state) {
      return state.movieTitles
    },
    comments(state) {
      return state.comments
    },
  },
  modules: {
  }
})
