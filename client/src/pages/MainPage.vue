<script setup lang="ts">
import { onBeforeMount, ref } from 'vue';
// import Canvas from '../components/Canvas.vue';
import router from "../router/index"
const isLogin = ref(true)

onBeforeMount(() => {
  if (!isLogin.value) {
    router.push("/login")
  }
})
</script>

<template>
  <div>
    <h1>Main Page</h1>
    <!-- <Canvas /> -->
  </div>
</template>