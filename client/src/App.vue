<script setup lang="ts">
import { RouterLink, RouterView, useRoute } from 'vue-router';
// import { usePooling } from './composables/pooling'

// const {x, y} = useMouse();
// const { data }= usePooling();
const route = useRoute();
</script>

<template>
  <div id="wrapper">
    <header id="app-header">
      <h1>App: {{ route.fullPath }}</h1>
      <nav>
       <RouterLink to="/login">Go to Login</RouterLink>
       <RouterLink to="/">Go to Main</RouterLink>
      </nav>
    </header>
    <main>
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
#wrapper {
  border: 1 solid #000;
}
#app-header {
  float: left;
}
</style>
