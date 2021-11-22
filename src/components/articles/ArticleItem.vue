<template>
  <div class="reviewitem">              
      <v-expansion-panel-header>
        <h2 >Article: {{articleItem.title }} </h2>   
        <!-- <h2 >작성자: {{ article.user.username }}</h2>    -->
      </v-expansion-panel-header>

        <v-expansion-panel-content>
        <textarea name="articleContent" cols="30" rows="10" v-model="articleItem.content" placeholder="내용"></textarea>
        </v-expansion-panel-content>
        <!-- <p>이 글을 좋아한 사람: {{ review.like_users }}</p> -->
        <hr>
        <p>작성 시각: {{ article.created_at | moment('from', 'now') }}</p>
        <p>수정 시각: {{ article.updated_at | moment('from', 'now') }}</p>  
      <v-expansion-panel-content>    
        <div><button class="btn btn-primary" @click="updateArticle">UPDATE</button></div>  
        <div><button class="btn btn-danger" @click="deleteArticle">DELETE</button></div>  
      </v-expansion-panel-content>
      <v-expansion-panel-content>  
      <comment-create :article="article"></comment-create>
      <comment-list :article="article">
      </comment-list>
      </v-expansion-panel-content> 
  </div>
</template>

<script>
import CommentList from '@/components/articles/CommentList'
import CommentCreate from '@/components/articles/CommentCreate'

export default {
  name: 'ArticleItem',
  components: {
    CommentList,
    CommentCreate,
  },
  props: {
    article: {
      type: Object,
      required: true
    },
  },  
  data: function () {
    return {
      articleItem: {  
        title: this.article.title,
        content: this.article.content,
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
    deleteArticle() {
      const deleteItem = {
        article_id: this.article.id,
        token: this.setToken()
      }      
      console.log(deleteItem)
      this.$store.dispatch('deleteArticle', deleteItem)
    },
    updateReview() {
      const updateItem = {
        articleItem: this.articleItem,
        article_id: this.article.id,
        token: this.setToken()
      }
      console.log(updateItem)  
      this.$store.dispatch("updateArticle", updateItem)    
    }

  },
  created() {
    console.log(this.article)
  }
}
</script>

<style >
.reviewitem{
  font-family: 'Noto Sans KR', sans-serif; 
}
</style>