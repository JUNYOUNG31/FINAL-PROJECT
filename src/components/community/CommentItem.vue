<template>
  <div>
    <v-text-field v-model="commentItem.content"></v-text-field>
    <span>댓글 작성일 : {{ comment.created_at | moment('YYYY-MM-DD HH:mm:ss') }}</span>
    <span>댓글 수정일 : {{ comment.updated_at | moment('YYYY-MM-DD HH:mm:ss') }}</span>
    <button class="btn btn-primary" @click="updateComment">댓글 수정</button>
    <button class="btn btn-danger" @click="deleteComment">댓글 삭제</button>

    <div v-if="commentLiked" class="comment-detail-like">
      <i @click="toggleLike" style="color: crimson" class="fas fa-heart comment-detail-like-button"></i> {{ likeUser.length }}
    </div>
    <div v-else class="comment-detail-like">
      <i @click="toggleLike" class="fas fa-heart comment-detail-like-button"></i> {{ likeUser.length }}
    </div>    

  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'CommentItem',
  props: {
    article: {
      type: Object,
      required: true,
    },
    comment: {
      type: Object,
      required: true,
    },

  },
  data() {
    return {
      commentItem: {
        content: this.comment.content
      },
      currentUser: null,
      likeUser: null,
      commentLiked: null,
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
        console.log(res)
        this.currentUser = res.data
        this.commentLiked = !!this.likeUser.some(user => user.username === this.currentUser.username)
      })
      .catch(err => console.log(err))
    },

    toggleLike() {
      const likeBtn = document.querySelector(".comment-detail-like-button")
      axios({
      method: 'POST',
      url: `${SERVER_URL}articles/${this.article.id}/${this.comment.id}/like/`,
      headers: this.setToken()})
      .then(res => {
        console.log(res)
        if (res.data.liked) {
          likeBtn.style.color = "crimson"
          this.likeUser.push(this.currentUser)
          }
      else {
          likeBtn.style.color = "black"
          this.likeUser = this.likeUser.filter(user => {
          return this.currentUser.username !== user.username
            })
        }
      })
      .catch(err=>console.log(err))
    },
    likedColor() {
      const likeBtn = document.querySelector(".comment-detail-like-button")
      console.log(this.commentLiked)
      if (this.commentLiked) {
          likeBtn.style.color = 'crimson'
      } else {likeBtn.style.color = 'black'}
    },

    getArticleComment(){
      axios({
      method: 'GET',
      url: `${SERVER_URL}articles/${this.article.id}/${this.comment.id}/`,
      headers: this.setToken()})
      .then(res => {
        console.log(res)
        this.comment = res.data
        this.likeUser = this.comment.like_users
      })
    },
    updateComment() {
      const commentItemSet = {
        commentItem: this.commentItem,
        comment_id: this.comment.id,
        article_id: this.article,
        token: this.setToken()
      }
      console.log(commentItemSet)
      this.$store.dispatch('updateArticleComment', commentItemSet)
    },
    deleteComment() {
      const commentItemSet = {
        comment_id: this.comment.id,
        article_id: this.article,
        token: this.setToken()
      }
      this.$store.dispatch('deleteArticleComment', commentItemSet)
    }
  },
  created() {
    this.getArticleComment()
    this.getCurrentUser()
  }
}
</script>

<style>
</style>