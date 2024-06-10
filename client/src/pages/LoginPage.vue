<script setup lang="ts">
import Message from '../components/Message.vue';
import { usePooling } from '../composables/pooling';

const {data} = usePooling();
</script>

<template>
  <div>
    <h1>Login Page</h1>
    <Message :data="data?.random" />
  </div>
</template>