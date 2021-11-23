<template>
  <div class="Community">
    <h2>Community</h2>
    <span v-if="isLogin">
      <article-create>
      </article-create>    
      <article-list>        
      </article-list>
    </span>    
    <router-view @login="isLogin = true"/>      
  </div>
</template>

<script>
import ArticleList from '@/components/community/ArticleList'
import ArticleCreate from '@/components/community/ArticleCreate'

export default {
  name: "Community",
  components: {
    ArticleList,
    ArticleCreate,
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