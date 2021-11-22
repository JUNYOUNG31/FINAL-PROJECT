<template>
  <div>
    <input type="text" class="input-box" placeholder="댓글 내용" v-model="commentItem.content">
    <button class="btn btn-create" @click="createComment">댓글 작성</button>
  </div>
</template>

<script>
export default {
  name: 'CommentCreate',
  props: {
    article: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      commentItem: {
        content: null,
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
    createComment() {
      const commentItemSet = {
        commentItem: this.commentItem,
        article_id: this.article.id,
        token: this.setToken()
      }
      this.$store.dispatch('createArticleComment', commentItemSet)
      this.commentItem.content = null
    },
  },
}
</script>

<style>
</style>