<template>
  <div>
    <template>
      <v-list class="plzmin">
        <v-list-item class="marginminus">
        <v-list-item-content class="marginminus2"> 
        <v-text-field v-model="commentItem.content"></v-text-field>
        </v-list-item-content>         
        </v-list-item>
        <v-list-item class="marginminus">
        <v-list-item-subtitle><span>작성일 : {{ comment.created_at | moment('YYYY-MM-DD HH:mm') }}</span>---------<span>수정일 : {{ comment.updated_at | moment('YYYY-MM-DD HH:mm') }}</span></v-list-item-subtitle>
        <v-btn class="btn btn-primary" @click="updateComment">UPDATE</v-btn>
        <v-btn class="btn btn-danger" @click="deleteComment">DELETE</v-btn>
        </v-list-item>
        <v-divider></v-divider>
      </v-list>
      </template>    
  </div>
</template>

<script>
export default {
  name: 'CommentItem',
  props: {
    review: {
      type: Number,
      required: true,
    },
    comment: {
      type: Object,
      required: true,
    }
  },
  data() {
    return {
      commentItem: {
        content: this.comment.content
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
    updateComment() {
      const commentItemSet = {
        commentItem: this.commentItem,
        comment_id: this.comment.id,
        review_id: this.review,
        token: this.setToken()
      }
      console.log(commentItemSet)
      this.$store.dispatch('updateComment', commentItemSet)
    },
    deleteComment() {
      const commentItemSet = {
        comment_id: this.comment.id,
        review_id: this.review,
        token: this.setToken()
      }
      this.$store.dispatch('deleteComment', commentItemSet)
    }
  },
}
</script>

<style>
.marginminus {
  height: 30px;
  box-sizing: border-box;
  padding: 0;
  margin-left: 5px;
}
.marginminus2 {
  height: 50px;
  box-sizing: border-box;
  padding: 0;
  margin-left: 5px;
}
.plzmin {
  min-height: 50px;
}
.plzmin .v-list-item {
  min-height: 45px;
}
</style>