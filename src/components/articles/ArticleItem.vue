<template>  
  <div class="articleitem">  
    <v-dialog v-model="dialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >            
    <template v-slot:activator="{ on, attrs }">
        <v-btn class="btnclass"
          color="primary"
          dark
          v-bind="attrs"
          v-on="on"
        >
        Article : {{articleItem.title }}
        </v-btn>
    </template>
     <v-card>
        <v-toolbar dark>          
          <v-toolbar-title>작성자: {{ article.user.username }}</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
            <v-btn
            icon
            dark
            @click="dialog = false"
            >
            <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-toolbar-items>
        </v-toolbar>
        <v-list
          four-line
          subheader
        >         
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>{{articleItem.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>  
          <v-list-item>            
            <v-list-item-content>
              <v-list-item-title>Content</v-list-item-title>
              <v-list-item-subtitle><textarea name="articleContent" cols="80" rows="5" v-model="articleItem.content" placeholder="내용"></textarea></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>          
          <v-list-item>    
          <v-spacer></v-spacer>   
          <v-spacer></v-spacer>    
          <v-subheader>작성 시각: {{ article.created_at | moment('from', 'now') }}</v-subheader>          
          <v-subheader>수정 시각: {{ article.updated_at | moment('from', 'now') }}</v-subheader>
            <v-list-item-content>
              <v-list-item-title>Likes</v-list-item-title>
              <v-list-item-subtitle>이 글을 좋아한 사람: {{ article.like_users }}</v-list-item-subtitle>
            </v-list-item-content>
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
    </v-dialog>

  <!-- <div class="reviewitem">              
      <v-expansion-panel-header>
        <h2 >Article: {{articleItem.title }} </h2>   
        <h2 >작성자: {{ article.user.username }}</h2>   
      </v-expansion-panel-header>

        <v-expansion-panel-content>
        <textarea name="articleContent" cols="30" rows="10" v-model="articleItem.content" placeholder="내용"></textarea>
        </v-expansion-panel-content>
        <p>이 글을 좋아한 사람: {{ review.like_users }}</p>
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
  </div> -->
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
      dialog : false
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
.articleitem {
  font-family: 'Noto Sans KR', sans-serif; 
}

.btnclass {
  
  margin: 8px;
}
</style>