<script setup lang="ts">
const props = defineProps<{
  price: number,
}>();
</script>

<template>
  <div class="flex">
    <span class="self-end text-lg text-green-500">{{ price/ 100 }}</span>
    <span class="self-start text-sm text-gray-700 ml-1">€</span>
  </div>
</template>