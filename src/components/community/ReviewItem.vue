<template>
  <div>              
      <v-expansion-panel-header>
        <h2 >리뷰 제목: {{ review.title }}</h2>   
        <!-- <h2 >작성자: {{ review.user.username }}</h2>    -->
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <p>영화 제목: {{ review.movie_title }}</p>
        <p>평점: {{ review.rank }}</p>
        <p>리뷰 내용: {{ review.content }}</p>
        <!-- <p>이 글을 좋아한 사람: {{ review.like_users }}</p> -->
        <hr>
        <p>작성 시각: {{ review.created_at }}</p>
        <p>수정 시각: {{ review.updated_at }}</p>      

        <div><button class="btn btn-danger" @click="deleteReview">DELETE</button></div>  
      </v-expansion-panel-content>
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: {
      type: Object,
      required: true
    },
  },  
  // data: function () {
  //   return {
  //     reviewItem: {
  //       movie_title: this.review.movie_title,        
  //       title: this.review.title,
  //       content: this.review.content,
  //       rank: this.review.rank,
  //       created_at: this.review.created_at,
  //       updated_at: this.review.updated_at,
  //       user: this.review.user,
  //       like_users: this.review.like_users
  //     },
  //   }
  // },
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
      this.$store.dispatch('deleteReview',deleteItem)
    }
  },
  created() {
    console.log(this.review)
  }
}
</script>

<style>

</style>