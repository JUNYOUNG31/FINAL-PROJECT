<template>
  <div class="reviewitems">   
    <v-card>
      <v-toolbar dark>   
        <v-spacer></v-spacer>       
        <v-toolbar-title>{{review.id}}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer> 
        <v-spacer></v-spacer>  
        <v-toolbar-title>{{review.user.username}}</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-spacer></v-spacer>
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
            <v-list-item-title>Title </v-list-item-title>
            <v-list-item-title>{{ review.title }}</v-list-item-title>
          </v-list-item-content>          
          <v-list-item-content>
            <v-list-item-title>Movie Title</v-list-item-title>
            <v-list-item-title>{{ review.movie_title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item>
          <v-list-item-content>
            <v-list-item-title>Rank              
            </v-list-item-title>
            <v-list-item-subtitle><v-rating
              v-model="review.rank"
              color="light-blue accent-"
              background-color="grey darken-1"
              empty-icon="$ratingFull"
              half-increments
              hover
              large
            ></v-rating></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
      <v-list subheader>          
        <v-list-item>            
          <v-list-item-content>
            <v-list-item-title>Content</v-list-item-title>            
            <v-list-item-title>
              <div class="marginplz">
              <v-textarea outlined name="reviewContent" cols="80" rows="5" v-model="review.content" placeholder="내용"></v-textarea>
              </div></v-list-item-title>
          </v-list-item-content>
        </v-list-item>          
        <v-list-item>    
        <v-spacer></v-spacer>   
        <v-spacer></v-spacer>    
        <v-subheader>작성 시각: {{ review.created_at | moment('from', 'now') }}</v-subheader>          
        <v-subheader>수정 시각: {{ review.updated_at | moment('from', 'now') }}</v-subheader>
          <v-list-item-content>
            <v-list-item-title>Likes</v-list-item-title>
            <v-list-item-subtitle>이 글을 좋아한 사람: {{ review.like_users }}</v-list-item-subtitle>
          </v-list-item-content>
          <v-spacer></v-spacer> 
          <v-spacer></v-spacer> 
          <v-list-item-content>
            <v-btn class="btn btn-primary" @click="updateReview">UPDATE</v-btn>
            <v-btn class="btn btn-danger" @click="deleteReview">DELETE</v-btn>
          </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
    <v-card max-width="900">
    <v-toolbar color="light-blue lighten-2">
      <v-spacer></v-spacer> 
      <v-toolbar-title>Comments</v-toolbar-title>
      <v-spacer></v-spacer>      
    </v-toolbar>
    <v-list three-line>
      <v-list-item>
        <v-list-item-content class="marginplz2">          
      <comment-create :review="review"></comment-create>
      </v-list-item-content>
      </v-list-item>
      <v-list-item>
      <v-list-item-content>
      <comment-list :review="review"></comment-list>
        </v-list-item-content>
      </v-list-item>      
    </v-list>
  </v-card>     
      </v-list>
    </v-card>
  </div>
</template>
<script>
import CommentList from '@/components/reviews/CommentList'
import CommentCreate from '@/components/reviews/CommentCreate'
import axios from 'axios'
const SERVER_URL = 'http://127.0.0.1:8000/'
export default {
  name: 'ReviewDetail',
  components: {
  CommentList,
  CommentCreate
  },
  data: function(){
    return  {
      review: null,
      // comment: null,
      reviewItem: {
        movie_title: null  ,  
        movie_pk: null,
        title: null,
        content: null,
        rank: null,
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
    deleteReview() {
      const deleteItem = {
        review_id: this.review.id,
        token: this.setToken()
      }      
      console.log(deleteItem)
      this.$store.dispatch('deleteReview', deleteItem)
    },
    updateReview() {
      this.reviewItem.movie_title= this.review.movie_title,      
      this.reviewItem.movie_pk= this.review.movie_pk,
      this.reviewItem.title= this.review.title,
      this.reviewItem.content= this.review.content,
      this.reviewItem.rank= this.review.rank,
      this.reviewItem.id =  this.review.id
      const updateItem = {
        reviewItem: this.reviewItem,
        review_id: this.review.id,
        token: this.setToken()
      }
      console.log(updateItem)  
      this.$store.dispatch("updateReview", updateItem)    
    },
    goback() {
      this.$router.push({name:'Reviews'})
    }
  },
  created(){
    this.getReview()
  }
}

</script>

<style>
.reviewitems {
  font-family: 'Noto Sans KR', sans-serif;    
  background-color: #0009;
  display: flex;
  flex-direction: column;
  align-items: left;   
  border-radius: 5px;
  box-sizing: border-box;
  width:900px;
  margin: 0;
  max-width: 900px;
  padding: 10px 30px 20px;  
}
.reviewitems .marginplz {
  margin-top: 10px;
}
.reviewitems .marginplz2 {
  margin-top: 10px;
  margin-bottom: 20px;
}
</style>