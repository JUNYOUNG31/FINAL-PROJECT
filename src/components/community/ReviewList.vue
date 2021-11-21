<template>
  <div>
    <p>리뷰 리스트</p>
    <v-expansion-panels>
      <v-expansion-panel    
    v-for="review in reviews" 
    :key="review.pk">    
    <review-item :review="review">
    </review-item>
    </v-expansion-panel> 
    </v-expansion-panels>
  </div>  
</template>

<script>
import ReviewItem from '@/components/community/ReviewItem'
import {mapGetters} from 'vuex'
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