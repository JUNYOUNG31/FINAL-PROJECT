<template>
<div>
      <div class="reviewitem">      
      <h2>
      REVIEW: {{review.title }}

      </h2>
      <h2>
      작성자: {{ review.user.username }}
      </h2>
      <h2>{{ review.title }}</h2>
      <h2>{{ review.movie_title }}</h2>             
        <!-- <v-rating
        v-model="reviewItem.rank"
        color="light-blue accent-"
        background-color="grey darken-1"
        empty-icon="$ratingFull"
        half-increments
        hover
        large
        ></v-rating>    -->
      <p>{{review.content}}</p>
      <!-- <textarea name="reviewContent" cols="80" rows="5" v-model="reviewItem.content" placeholder="내용"></textarea> -->

      <p>작성 시각: {{ review.created_at | moment('from', 'now') }}</p>          
      <p>수정 시각: {{ review.updated_at | moment('from', 'now') }}</p>

      <p>Likes</p>
      <p>이 글을 좋아한 사람: {{ review.like_users }}</p>
      <v-btn class="btn btn-primary" @click="updateReview">UPDATE</v-btn>
      <v-btn class="btn btn-danger" @click="deleteReview">DELETE</v-btn>               
      </div>

    <button @click="getReview">ewqewqewqewqewq</button>
    <h2></h2>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'ReviewDetail',
  data: function(){
    return  {
      review: null,
      // comment: null,
      // reviewItem: {
      //   movie_title: this.review.movie_title,      
      //   movie_pk: this.review.pk,
      //   title: this.review.title,
      //   content: this.review.content,
      //   rank: this.review.rank,
      //   id: this.review.id
      // },
    }
  },
  methods : {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getReview(){
      axios({
      method: 'GET',
      url: `${SERVER_URL}movies/community/${this.$route.params.id}/`,
      headers: this.setToken()})
      .then(res => {
        console.log(res)
        this.review = res.data
      })
    },
    // deleteReview() {
    //   const deleteItem = {
    //     review_id: this.review.id,
    //     token: this.setToken()
    //   }      
    //   console.log(deleteItem)
    //   this.$store.dispatch('deleteReview', deleteItem)
    // },
    // updateReview() {
    //   const updateItem = {
    //     reviewItem: this.reviewItem,
    //     review_id: this.review.id,
    //     token: this.setToken()
    //   }
    //   console.log(updateItem)  
    //   this.$store.dispatch("updateReview", updateItem)    
    // }
  },
  created(){
    this.getReview()
  }
  // mounted() {
  //   this.getReview()
  // }

}

</script>

<style>

</style>