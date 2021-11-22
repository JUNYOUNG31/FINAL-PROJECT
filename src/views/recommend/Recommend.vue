<template>
  <div>
    <h2>추천 알고리즘</h2>
    <button @click="recommendmovie">???</button>
    <div v-for="(movie, idx) in movies_list" 
    :key="idx">
    <v-img :src="`https://www.themoviedb.org/t/p/original/${movie.backdrop_path}`" alt="movie_poster">
    </v-img>
    <hr>
    </div>
    
  </div>  
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'

export default {
  name: 'Recommend',   
  data: function () {
    return {
      movies_list : null,
      items: {
        title: null,
        poster: null,
        overview: null,

      }
    }
  },
  
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    recommendmovie() {
      axios({
        method: 'GET',
        url: `${SERVER_URL}movies/recommend/`,
        headers : this.setToken()
      })
      .then(res => {
        console.log(res)
        const recommendmovie_id = res.data.pk
        axios({
        method: 'GET',
        url: `https://api.themoviedb.org/3/movie/${recommendmovie_id}/recommendations?api_key=16d1729d729f6d8c5d36bfaba0aee1a6&language=ko-KR&page=1`,
        })
        .then(res=> {
          console.log(res)
          this.movies_list = res.data.results
        })
      })      
      .catch(err => { 
        console.log(err)        
      })
    } 
  }
}
</script>

<style>

</style>