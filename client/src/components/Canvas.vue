<script setup lang="ts">

import {ref,  onMounted, onUnmounted} from 'vue'
const canvasRef = ref<HTMLCanvasElement | null>(null)
const ctx = ref<CanvasRenderingContext2D | null>(null)

onMounted(() => {
  if (canvasRef.value) {
    canvasRef.value.width = window.innerWidth
    canvasRef.value.height = window.innerHeight
    ctx.value = canvasRef.value.getContext('2d')
    canvasRef.value.addEventListener('mousedown', mouseDown);
  }
  loop()
})

onUnmounted(() => {
  if (canvasRef.value) {
    canvasRef.value.removeEventListener('mousedown', mouseDown)
  }
})

const loop = () => {
  if (canvasRef.value && ctx.value) {
    ctx.value.fillStyle = "#cccccc"
    ctx.value.fillRect(0, 0, canvasRef.value.width, canvasRef.value.height)
  }
}

const pos = (e: MouseEvent) => {
  if (!canvasRef.value) return
  return {
    x: e.clientX - canvasRef.value?.getBoundingClientRect().left,
    y: e.clientY - canvasRef.value?.getBoundingClientRect().top,
  }
}

const mouseDown = (e: MouseEvent) => {
  const p = pos(e);
  if (canvasRef.value && ctx.value && p) {
    ctx.value.fillStyle = "#ffffff"
    ctx.value.fillRect(p.x, p.y, 15, 15);
  }
}
</script>

<template>
  <canvas ref="canvasRef"></canvas>
</template>

<style scoped>
</style>

