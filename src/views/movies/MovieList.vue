<template>
  <div>
  <p>영화 리스트</p>
  <p v-for="movie in movies" :key="movie.title">
    {movie.title}
  </p>
  </div>
  
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'MovieList',  
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