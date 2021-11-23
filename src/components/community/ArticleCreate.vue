<template>
  <v-dialog
        v-model="dialog"
        persistent
        max-width="600px"
      >
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="#831010" dark v-bind="attrs" v-on="on">
          게시글 작성하기
        </v-btn>
      </template>
      <v-card dark>
        <v-card-title>
          <span class="headline">Article Form</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  label="제목*"
                  v-model.trim="articleItem.title"
                  required
                ></v-text-field>
              </v-col>

              <v-col cols="12">
                <v-textarea
                  solo
                  label="*내용"
                  v-model.trim="articleItem.content"
                  required
                ></v-textarea>
              </v-col>
            </v-row>
          </v-container>
          <small>*이용수칙에 맞지 않는 게시글의 경우 사전 고지 없이 삭제 될 수 있습니다.</small>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            닫기
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="createArticle"
          >
            저장
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>
export default {
  name: 'ArticleCreate',  
  data() {
    return {
      articleItem: {
        title: null,
        content: null,
      },
      dialog: false,
    }
  },
  methods: {
    setToken() {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createArticle() {     
      const articlecreate = {
      articleItem: this.articleItem,      
      token: this.setToken()
    }
    this.$store.dispatch('createArticle', articlecreate)
    this.title = null,
    this.content = null,
    this.dialog = false    
    }
  },
}
</script>

<style>

</style>