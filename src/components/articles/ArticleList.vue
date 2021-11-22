<template>
  <div>
    <p>게시글 리스트</p>
    <v-expansion-panels>
      <v-expansion-panel    
    v-for="(article, id) in articles" 
    :key="id">    
    <article-item :article="article">
    </article-item>
    </v-expansion-panel> 
    </v-expansion-panels>
  </div>  
</template>

<script>
import {mapGetters} from 'vuex'
import ArticleItem from '@/components/articles/ArticleItem'
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

</style>