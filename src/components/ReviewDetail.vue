<template>
  <div>    
    <h1>{{ review.title }}</h1>       
    <p>{{ review.content }}</p>
  </div>
</template>

<script>
export default {
  name: 'ReviewDetail',
  props: {
    review: {
      type: Object,
      required: true
    },
  },
}
</script>

<style>

</style>