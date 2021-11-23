<template>
  <div>
    <comment-item
      v-for="(comment, idx) in comments"
      :key="idx"
      :comment="comment"
      :review="reviewdetail"
    >
    </comment-item>
  </div>
</template>

<script>
import CommentItem from '@/components/reviews/CommentItem'
import { mapGetters } from 'vuex'
export default {
  name: 'CommentList',
  props: {
    review: {
      type: Object,
      required: true,
    }
  },
  data () {
    return {
      reviewdetail: this.review.id
    }
  },
  components: {
    CommentItem
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
  },
  computed: {
    ...mapGetters([
      'comments'
    ])
  },
  created() {
    const commentListSet = {
      review_id: this.review.id,
      token: this.setToken()
    }
    console.log(commentListSet)
    this.$store.dispatch('getComments', commentListSet)
  },
}
</script>

<style>

</style>