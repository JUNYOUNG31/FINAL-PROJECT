<template>
  <div class="reviewitem">              
      <v-expansion-panel-header>
        <h2 >REVIEW: {{reviewItem.title }} </h2>   
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
      <v-expansion-panel-content>  
      <comment-create :review="review"></comment-create>
      <comment-list :review="review">
      </comment-list>
      </v-expansion-panel-content> 
  </div>
</template>

<script>
import CommentList from '@/components/community/CommentList'
import CommentCreate from '@/components/community/CommentCreate'

export default {
  name: 'ReviewItem',
  components: {
    CommentList,
    CommentCreate
  },
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
      this.$store.dispatch('deleteReview', deleteItem)
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

<style >
.reviewitem{
  font-family: 'Noto Sans KR', sans-serif; 
}
</style>