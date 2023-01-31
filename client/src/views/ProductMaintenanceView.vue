<script setup lang="ts">
import PMSidebar from '@/components/PMSidebar.vue';
</script>

<template>
  <div class="flex">
    <PMSidebar class="min-w-fit" />
    <RouterView />
  </div>
</template>
