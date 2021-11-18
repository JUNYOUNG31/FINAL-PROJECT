<template>
  <div class="col-mb-6">    
      <h1>{{ movie.title }}</h1>        
      <img :src="`https://www.themoviedb.org/t/p/w500/${movie.poster_path}`" alt="movie_poster"> 
      <p>{{ movie.genre_ids }}</p>
      <p>{{ movie.overview }}</p>    
  </div>
</template>

<script>
export default {
  name: 'MovieDetail',
  props: {
    movie: {
      type: Object,
      required: true
    },
  },
}
</script>

<style>

</style>