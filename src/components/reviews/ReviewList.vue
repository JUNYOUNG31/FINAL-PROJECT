<template>
  <div class="reviewlist">
    <p>list</p>

    <div class="reviewitems"> 
      <div v-for="(review, id) in reviews" 
    :key="id" class="review_item">
      <v-row justify="center">      
        <review-item :review="review">
        </review-item>
      </v-row>
      </div>
    </div>

    <!-- <v-expansion-panels class="reviewitems">
      <v-expansion-panel    
    v-for="(review, id) in reviews" 
    :key="id" class="review_item">    
    <review-item :review="review">
    </review-item>
    </v-expansion-panel> 
    </v-expansion-panels> -->
  </div>  
</template>

<script>
import {mapGetters} from 'vuex'
import ReviewItem from '@/components/reviews/ReviewItem'
export default {
  name: 'ReviewList',  
  components: {
    ReviewItem
  },    
  computed: {
    ...mapGetters(['reviews'])
  },
  created() {
    this.$store.dispatch('getReviews')
  },
}
</script>

<style>
.reviewlist {
  font-family: 'Noto Sans KR', sans-serif;    
  background-color: #0009;
}
.reviewitems{
  padding: 0 50px;
}
.review_item{
  padding: 5px;
}
</style>