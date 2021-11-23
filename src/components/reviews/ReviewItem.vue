<template>
  <div class="reviewitem">  
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
        REVIEW: {{reviewItem.title }}
        </v-btn>
    </template>
     <v-card>
        <v-toolbar dark>          
          <v-toolbar-title>작성자: {{ review.user.username }}</v-toolbar-title>
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
          three-line
          subheader
        >         
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>{{ review.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>{{ review.movie_title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Rank :              
              </v-list-item-title>
              <v-list-item-subtitle><v-rating
                v-model="reviewItem.rank"
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
        <v-list
          three-line
          subheader
        >          
          <v-list-item>            
            <v-list-item-content>
              <v-list-item-title>Content</v-list-item-title>
              <v-list-item-subtitle><textarea name="reviewContent" cols="80" rows="5" v-model="reviewItem.content" placeholder="내용"></textarea></v-list-item-subtitle>
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
          <v-list-item>            
            <v-list-item-content>
              <comment-create :review="review"></comment-create>
              <comment-list :review="review">
              </comment-list>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import CommentList from '@/components/reviews/CommentList'
import CommentCreate from '@/components/reviews/CommentCreate'

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
        movie_pk: this.review.pk,
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank,
        
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
.reviewitem >h2{
  font-family: 'Noto Sans KR', sans-serif;   
}

.btnclass {
  
  margin: 8px;
}
</style>