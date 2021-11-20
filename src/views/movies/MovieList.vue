<template>
  <div class="movieform">
    <h2>MOVIE LIST</h2>
    <movie-item 
    v-for="movie in movies" 
    :key="movie.pk"
    :movie="movie">   
    </movie-item>
  </div>  
</template>

<script>
import MovieItem from '@/components/MovieItem'
import { mapGetters } from 'vuex'
export default {
  name: 'MovieList',  
  components: {
    MovieItem
  },
  methods: {      
  },
  computed: {
    ...mapGetters(['movies'])
  },
  created() {
    this.$store.dispatch('getMovies')
  },

}
</script>

<style>
.movieform h2{
  font-family: 'Bebas Neue', cursive;
  color: lightskyblue
}
</style>