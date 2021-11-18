<template>
  <div>
    <p>리뷰 리스트</p>
    <review-detail 
    v-for="review in reviews" 
    :key="review.pk"
    :review="review">   
    </review-detail>
  </div>  
</template>

<script>
import ReviewDetail from '@/components/ReviewDetail'
import {mapGetters} from 'vuex'
export default {
  name: 'ReviewList',  
  components: {
    ReviewDetail
  },  
  methods: {   
    
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