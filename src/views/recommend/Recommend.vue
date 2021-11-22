<template>
  <p>dd</p>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Recommend',  
  
  computed: {
    ...mapGetters(['reviews'])
  },
  created() {    
    this.$store.dispatch('getReivews')
  }
}
</script>

<style>

</style>