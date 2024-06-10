<script setup lang="ts">

import {ref,  onMounted, watch} from 'vue'
const canvasRef = ref<HTMLCanvasElement | null>(null)
const ctx = ref<CanvasRenderingContext2D | null>(null)

const clear = () => {
  if (ctx.value && canvasRef.value) {
    ctx.value.fillStyle = "#cccccc"
    ctx.value.fillRect(0, 0, canvasRef.value.width, canvasRef.value.height)
  }
}

onMounted(() => {
  if (canvasRef.value) {
    canvasRef.value.width = window.innerWidth
    canvasRef.value.height = window.innerHeight - 300 
    ctx.value = canvasRef.value.getContext('2d')
  }
  clear()
})
watch(() => canvasRef.value, () => {
  console.log("change canvas")
}, {deep: true})
</script>

<template>
  <!-- <p>w: {{ width }} h: {{ height }} </p> -->
  <canvas
    id="canvas"
    ref="canvasRef"
  ></canvas>
</template>

<style scoped>
#canvas {
  width: 100%;
  margin: 0;
  padding: 0;
}
</style>

