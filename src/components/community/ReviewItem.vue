<template>
  <div>              
      <v-expansion-panel-header>
        <v-alert v-model="reviewItem.title"></v-alert>   
        <h2 >작성자: {{ review.user.username }}</h2>   
      </v-expansion-panel-header>
      <v-expansion-panel-content>영화 제목: {{ review.movie_title }}</v-expansion-panel-content>
      <v-expansion-panel-content>별점 :
        <v-rating
          v-model="reviewItem.rank"
          color="yellow darken-3"
          background-color="grey darken-1"
          empty-icon="$ratingFull"
          half-increments
          hover
          large
        ></v-rating>
      </v-expansion-panel-content>
        <v-expansion-panel-content>
        <textarea name="reviewContent" cols="30" rows="10" v-model="reviewItem.content" placeholder="내용"></textarea>
        </v-expansion-panel-content>
        <!-- <p>이 글을 좋아한 사람: {{ review.like_users }}</p> -->
        <hr>
        <p>작성 시각: {{ review.created_at | moment('from', 'now') }}</p>
        <p>수정 시각: {{ review.updated_at | moment('from', 'now') }}</p>  
      <v-expansion-panel-content>    
        <div><button class="btn btn-primary" @click="updateReview">UPDATE</button></div>  
        <div><button class="btn btn-danger" @click="deleteReview">DELETE</button></div>  
      </v-expansion-panel-content>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'ReviewItem',
  props: {
    review: {
      type: Object,
      required: true
    },
  },  
  data: function () {
    return {
      reviewItem: {
        movie_title: this.review.movie_title,      
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank,

      },
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
    deleteReview() {
      const deleteItem = {
        review_id: this.review.id,
        token: this.setToken()
      }      
      console.log(deleteItem)
      axios({
        method: 'DELETE',
        url: `${SERVER_URL}movies/community/${deleteItem.review_id}`,        
        headers: deleteItem.token
      })
      .then(res => {       
        console.log(res)
        this.$router.push({name:'Community'}) 
        this.$router.go()             
      }) 
    },
    updateReview() {
      const updateItem = {
        reviewItem: this.reviewItem,
        review_id: this.review.id,
        token: this.setToken()
      }
      console.log(updateItem)  
      this.$store.dispatch("updateReview", updateItem)    
    }

  },
  created() {
    console.log(this.review)
  }
}
</script>

<style>

</style>