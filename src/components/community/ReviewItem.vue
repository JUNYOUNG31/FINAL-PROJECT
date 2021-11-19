<template>
  <div>
    <v-expansion-panels>
    <v-expansion-panel
    >
      <v-expansion-panel-header>
        <h2 >리뷰 제목: {{ reviewItem.title }}</h2>   
        <h2 >작성자: {{ reviewItem.user.username }}</h2>   
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        <p>영화 제목: {{ reviewItem.movie_title.title }}</p>
        <p>평점: {{ reviewItem.rank }}</p>
        <p>리뷰 내용: {{ reviewItem.content }}</p>
        <p>이 글을 좋아한 사람: {{ reviewItem.like_users }}</p>
        <hr>
        <p>작성 시각: {{ reviewItem.created_at }}</p>
        <p>수정 시각: {{ reviewItem.updated_at }}</p>
        <p>장르 : {{ reviewItem.genre }}</p>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>    
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
        genre: this.review.movie_title.genre_ids,
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank,
        created_at: this.review.created_at,
        updated_at: this.review.updated_at,
        user: this.review.user,
        like_users: this.review.like_users
      },
    }
  },
  methods: {

  }
}
</script>

<style>

</style>