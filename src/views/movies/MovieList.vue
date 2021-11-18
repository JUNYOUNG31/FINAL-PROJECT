<template>
  <div>
    <p>영화 리스트</p>
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

</style>