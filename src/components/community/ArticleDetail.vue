<template>
  <div class="articleitems">   
    <v-card>
      <v-toolbar dark>          
        <v-spacer></v-spacer>
        <v-toolbar-items>
          <v-btn icon dark @click="goback">
          <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-toolbar-items>
      </v-toolbar>
      <v-list three-line>         
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>{{ article.title }}</v-list-item-title>
          </v-list-item-content>    
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list three-line subheader>          
        <v-list-item>            
          <v-list-item-content>
            <v-list-item-title>Content</v-list-item-title>            
            <v-list-item-title>
              <v-textarea outlined name="articleContent" cols="80" rows="5" v-model="article.content" placeholder="내용"></v-textarea>
              </v-list-item-title>
          </v-list-item-content>
        </v-list-item>          
        <v-list-item>    
        <v-spacer></v-spacer>   
        <v-spacer></v-spacer>    
        <v-subheader>작성 시각: {{ article.created_at | moment('from', 'now') }}</v-subheader>          
        <v-subheader>수정 시각: {{ article.updated_at | moment('from', 'now') }}</v-subheader>
          <!-- <v-list-item-content>
            <v-list-item-title>Likes</v-list-item-title>
            <v-list-item-subtitle>이 글을 좋아한 사람: {{ article.like_users }}</v-list-item-subtitle>
          </v-list-item-content> -->
          <v-spacer></v-spacer> 
          <v-spacer></v-spacer> 
          <v-list-item-content>
            <v-btn class="btn btn-primary" @click="updateArticle">UPDATE</v-btn>
            <v-btn class="btn btn-danger" @click="deleteArticle">DELETE</v-btn>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item>            
          <v-list-item-content>
            <comment-create :article="article"></comment-create>
            <comment-list :article="article">
            </comment-list>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card>
  </div>
</template>

<script>
import CommentList from '@/components/community/CommentList'
import CommentCreate from '@/components/community/CommentCreate'
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'ArticleDetail',
  components: {
  CommentList,
  CommentCreate
  },
  data: function(){
    return  {
      article: null,
      // comment: null,
      articleItem: {   
        title: null,
        content: null,        
        id: null
      },
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
    getArticle(){
      axios({
      method: 'GET',
      url: `${SERVER_URL}articles/${this.$route.params.id}/`,
      headers: this.setToken()})
      .then(res => {
        console.log(res)
        this.article = res.data
      })
    },
    deleteArticle() {
      const deleteItem = {
        article_id: this.article.id,
        token: this.setToken()
      }      
      console.log(deleteItem)
      this.$store.dispatch('deleteArticle', deleteItem)
    },
    updateArticle() {          
      this.articleItem.title= this.article.title,
      this.articleItem.content= this.article.content,      
      this.articleItem.id =  this.article.id
      const updateItem = {
        articleItem: this.articleItem,
        article_id: this.article.id,
        token: this.setToken()
      }
      console.log(updateItem)  
      this.$store.dispatch("updateArticle", updateItem)     
    },
    goback() {
      this.$router.push({name:'Community'})
    }
  },
  created(){
    this.getArticle()
  }
}

</script>

<style>

</style>