<template>
  <div class="articlewlist">
    <p>Article list</p>
    <div class="articleitems"> 
      <div v-for="(article, id) in articles" 
    :key="id" class="article_item">   
    <v-row justify="center">   
    <article-item :article="article">
    </article-item>
    </v-row>
  </div>  
  </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import ArticleItem from '@/components/community/ArticleItem'
export default {
  name: 'ArticleList',  
  components: {
    ArticleItem,
  },    
  computed: {
    ...mapGetters(['articles'])
  },
  created() {
    this.$store.dispatch('getArticles')
  },
}
</script>

<style>
.articlewlist {
  font-family: 'Noto Sans KR', sans-serif;    
  background-color: #0009;
}
.articleitems{
  padding: 0 50px;
}
.article_item{
  padding: 5px;
}
</style>