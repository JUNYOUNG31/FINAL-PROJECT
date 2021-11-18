<template>
  <div>
    <p>영화 리스트</p>
    <movie-detail 
    v-for="movie in movies" 
    :key="movie.pk"
    :movie="movie">   
    </movie-detail>
  </div>  
</template>

<script>
import MovieDetail from '@/components/MovieDetail'
import { mapGetters } from 'vuex'
export default {
  name: 'MovieList',  
  components: {
    MovieDetail
  },
  methods: {   
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
  computed: {
    ...mapGetters(['movies'])
  },
  created() {
    this.$store.dispatch('getMovies', this.setToken())
  },

}
</script>

<style>

</style>