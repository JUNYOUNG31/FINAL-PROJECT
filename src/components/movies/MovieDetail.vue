<template>
<div class="detailbtn">
  <v-row>
    <v-dialog
      v-model="dialog"
      fullscreen
      hide-overlay
      dark
      transition="dialog-bottom-transition"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn  class="detailbtn"
          v-bind="attrs"
          v-on="on" 
        >Movie Detail
        </v-btn>
      </template>
      <v-card class="moviedetailcard">
        <v-toolbar dark>   
          <v-spacer></v-spacer>
          <v-toolbar-title>{{ Movietitle}}</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-btn
            icon
            dark
            @click="dialog = false"
          ><v-icon>mdi-close</v-icon>
          </v-btn>          
        </v-toolbar>
        <v-img 
        max-height="700"
        max-width="350"
        :src="`https://www.themoviedb.org/t/p/w500/${movie.poster_path}`" alt="movie_poster">
        </v-img>
        <v-spacer></v-spacer>
        <v-list
          three-line          
        >          
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>{{movie.overview}}</v-list-item-title>
              <v-list-item-title>{{movie.genre_ids}}</v-list-item-title>
              <v-list-item-subtitle>{{movieall}}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>          
        </v-list>   
      </v-card>
    </v-dialog>
  </v-row>
  </div>
</template>

<script>
export default {
  name: 'MovieDetail',
  props: {
    movie: {
    type: Object,
    required: true
    }
  },
  data () {
      return {
        movieall: this.movie,
        Movietitle: this.movie.title,
        dialog: false,
      }
    },
}
</script>

<style>
.detailbtn {
  display: flex;
  align-items: center;
  display: inline-block;
  text-decoration: none;
  color: white;
  background: #0009;
  padding: 10px 15px;
}
.moviedetailcard {
  display: flex;
  
}
</style>