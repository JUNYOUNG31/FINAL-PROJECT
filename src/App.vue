<template>
  <v-app>

    <div id="nav">
      <span v-if="isLogin">
        <!-- <router-link :to="{ name: 'Profile' }">Profile</router-link>| -->
        <!-- <router-link :to="{ name: 'Community' }">Community</router-link>| -->
        <router-link @click.native="logout" to="#">Logout</router-link>|
        <router-link :to="{ name: 'MovieList' }">MovieList</router-link>|
        <router-link :to="{ name: 'ReviewList' }">Community</router-link>
      </span>
      <span v-else>
        <router-link :to="{ name: 'Signup' }">Signup</router-link>|
        <router-link :to="{ name: 'Login' }">Login</router-link>|
        <router-link :to="{ name: 'MovieList' }">MovieList</router-link>|
        <router-link :to="{ name: 'ReviewList' }">Community</router-link>
      </span>
    </div>
    <router-view @login="isLogin=true"/>

  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
