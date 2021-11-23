<template>
<div class="detailbtn">
  <v-row>
    <v-dialog
      v-model="dialog"      
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
          <v-spacer></v-spacer>
          <v-btn
            icon
            dark
            @click="dialog = false"
          ><v-icon>mdi-close</v-icon>
          </v-btn>          
        </v-toolbar>
        <v-container class="detail_container"><v-row>
          <v-col cols="5">
          <img class="detailimg"
          max-height="700"
          max-width="350"
          :src="`https://www.themoviedb.org/t/p/w500/${movie.poster_path}`" alt="movie_poster">
          </v-col>
          <v-col cols="7">
            <v-list>
              <v-list-item-content>
              <h2>{{ Movietitle}}</h2>
              </v-list-item-content>
              <v-list-item-content v-for="genre in movie.genre_ids"
                :key="genre.id">
                <v-span>,{{genre.name}}</v-span>
              </v-list-item-content>
              <v-rating
                  v-model="rank"                  
                  color="light-blue accent-"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  half-increments
                  hover
                  large
                  readonly
                ></v-rating>
                <v-list-item-content>
              <p>{{movie.release_date}}</p>
              </v-list-item-content>
              <v-list-item-content><p>{{movie.overview}}</p></v-list-item-content>
            </v-list>
          </v-col>
            </v-row></v-container>        
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
        rank: (Math.round(this.movie.vote_average))/2,
        dialog: false,
      }
    },
}
</script>

<style >
.detail_container{
  margin: 50px;
}
.detailbtn {
  display: flex;
  align-items: center;
  display: inline-block;
  text-decoration: none;
  color: white;
  background: #0009;
  padding: 10px 15px;
}

.detailimg {
  max-width: 100%;
  height: 90%;
  display: block;
  object-fit: cover;
}
p {    
  white-space: normal;
}
</style>