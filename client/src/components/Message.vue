<script setup lang="ts">
import { useCounterStore } from '../stores/counter'
import { useMouse } from '../composables/mouse'

const props = defineProps({
  data: Number
})

const store = useCounterStore()
const { x, y } = useMouse()
</script>

<template>
  <div class="child">
    <h1>{{ store.count }}</h1>
    <h1>{{ props.data }}</h1>
    <h2>{{ store.doubleCount }}</h2>
    <h3>Mouse position is at: {{ x }} {{ y }}</h3>
    <button @click="store.increment">Count</button>
  </div>
</template>

<style scoped>
.child {
  border: 1px solid #111111;
  text-align: center;
}
</style>