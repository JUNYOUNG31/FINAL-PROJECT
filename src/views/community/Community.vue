<template>
  <div class="Community">
    <h2>REVIEWS</h2>
    <span v-if="isLogin">    
      <review-create>
      </review-create>
      <review-list>        
      </review-list>
    </span>
    <span v-else>          
      <review-list>        
      </review-list>    
    </span>
    <router-view @login="isLogin = true"/>      
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList'
import ReviewCreate from '@/components/community/ReviewCreate'
export default {
  name: "Community",
  components: {
    ReviewList,
    ReviewCreate
  },
  data: function () {
    return {
      isLogin: false
    }
  },  
  created: function () {
    const token = localStorage.getItem('jwt')

    if(token) {
      this.isLogin = true
    }
  }
}
</script>

<style>
.Community h2{
  font-family: 'Bebas Neue', cursive;
  color: lightskyblue
}
</style>