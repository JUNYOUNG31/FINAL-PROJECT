<template>
  <div>    
    <hr>
    <h2>{{ reviewItem.title }}</h2>   
    <p>{{ reviewItem.movie_title.title }}</p>
    <p>{{ reviewItem.rank }}</p>
    <p>{{ reviewItem.content }}</p>
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: {
      type: Object,
      required: true
    },
  },  
  data: function () {
    return {
      reviewItem: {
        movie_title: this.review.movie_title,
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank,
      },
    }
  }
}
</script>

<style>

</style>