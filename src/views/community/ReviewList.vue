<template>
  <div>
    <p>리뷰 리스트</p>
    <review-item 
    v-for="review in reviews" 
    :key="review.pk"
    :review="review">
    </review-item>
  </div>  
</template>

<script>
import ReviewItem from '@/components/ReviewItem'
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