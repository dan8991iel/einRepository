<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
</script>

<template>
  <div class="pt-20">
    <nav class="fixed top-0 left-0 right-0 w-full h-20 p-4 bg-white shadow-md">
      <div class="text-center">
        <h1 class="text-xl text-green-500">Cookie-free Shop</h1>
        <div class="text-sm text-gray-500">We don't have cookies. Pinky promise!</div>
      </div>
    </nav>
    <RouterView />
  </div>
</template>
