<script setup lang="ts">
import { computed } from 'vue';
import Message from './components/Message.vue'
import { useMouse } from './composables/mouse'
import { usePooling } from './composables/pooling'

const {x, y} = useMouse();
const { data }= usePooling();
</script>

<template>
  <div>
    <h1>X: {{ x }} Y: {{ y }}</h1>
    <h2>POOLING DATA: {{ data?.random }}</h2>
    <Message />
  </div>
</template>

<style scoped>
</style>
