<template>
  <div class="movie_container">
    <div class="movielist">    
        <img :src="`https://www.themoviedb.org/t/p/original/${movie.poster_path}`" alt="movie_poster">         
        <div class="content">
          <h1>{{ movie.title }}</h1>        
          <p>{{ movie.overview }}</p>    
          <!-- <p>{{ movie.genre_ids }}</p> -->          
          <movie-detail
          :movie="moviedetail">   
          </movie-detail>
        </div>
    </div>
  </div>
</template>

<script>
import MovieDetail from '@/components/movies/MovieDetail'
export default {
  name: 'MovieItem',
  props: {
    movie: {
      type: Object,
      required: true
    },
  },
  components: {
    MovieDetail
  },
  data () {
      return {
        moviedetail: this.movie
      }
    },
}
</script>

<style>
.movie_container {
  width: 100%;
  height: 800px;
  position: relative;
}

.movielist {
  width: 100%;
  height: 100%;
  position: relative;
  animation: fade 1s ease-in-out;
}
@keyframes fade{
  to{
    opacity: 1;
  }
  from{
    opacity: 0;
  }
}

.movielist img{
  max-width: 1200px;
  height: 100%;
  display: block;
  object-fit: cover;
  filter: brightness(80%);
}

.movielist .content {
  position: absolute;
  left: 50px;
  bottom: 100px;
  color: white;
  max-width: 500px;
  text-shadow: 0 0 1px #000;  
  text-align: left;
}

.movielist .content h1{
  font-size: 2em;  
}

.movielist .content p{
  /* 한 줄 자르기 */ 
  display: inline-block;
  width: 500px; 
  white-space: nowrap; 
  overflow: hidden; 
  text-overflow: ellipsis;
  /* 여러 줄 자르기 추가 스타일 */
  white-space: normal; 
  line-height: 1.2; 
  height: 3.6em; 
  text-align: left; 
  word-wrap: break-word; 
  display: -webkit-box; 
  -webkit-line-clamp: 3; 
  -webkit-box-orient: vertical;
}

.movielist .content a:hover{
  background: lightskyblue;
}
</style>