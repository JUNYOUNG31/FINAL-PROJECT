<template>
  <div>
    <p>리뷰 리스트</p>
    <v-expansion-panels>
      <v-expansion-panel    
    v-for="(review, id) in reviews" 
    :key="id">    
    <review-item :review="review">
    </review-item>
    </v-expansion-panel> 
    </v-expansion-panels>
  </div>  
</template>

<script>
import {mapGetters} from 'vuex'
import ReviewItem from '@/components/community/ReviewItem'
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

</style>