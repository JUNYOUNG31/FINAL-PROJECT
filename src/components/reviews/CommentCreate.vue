<template>
  <div>
    <input type="text" class="input-box" placeholder="댓글 내용" v-model="commentItem.content">
    <button class="btn btn-create" @click="makeCreate">댓글 작성</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'CommentCreate',
  props: {
    review: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      commentItem: {
        content: null,
        currentUser: null,
      }
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
    getCurrentUser() {
      axios({
        method: 'GET',
        url: `${SERVER_URL}accounts/`, 
        headers: this.setToken()
      }) 
      .then(res => {
        
        this.commentItem.currentUser = res.data.username    
        console.log(this.commentItem.currentUser)
      })
      .catch(err => console.log(err))
    },    
    createComment() {
      const commentItemSet = {
        commentItem: this.commentItem,
        review_id: this.review.id,
        token: this.setToken()
      }
      console.log(commentItemSet)
      this.$store.dispatch('createComment', commentItemSet)
      this.commentItem.content = null
      this.commentItem.currentUser = null
    },
    makeCreate () {
      this.getCurrentUser()
      this.createComment()
    }
  },
}
</script>

<style>
</style>