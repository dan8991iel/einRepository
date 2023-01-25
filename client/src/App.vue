<script setup lang="ts">
import { RouterView } from "vue-router";
import NavBar from "./components/NavBar.vue";
</script>

<template>
  <div class="pt-20">
    <NavBar />
    <RouterView />
  </div>
</template>
