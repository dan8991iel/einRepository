<script setup lang="ts">
import PMSidebar from '@/components/PMSidebar.vue';
</script>

<template>
  <div class="md:flex">
    <PMSidebar class="min-w-fit" />
    <RouterView />
  </div>
</template>
