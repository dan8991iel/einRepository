<script setup lang="ts">
defineProps<{
  price: number;
}>();
</script>

<template>
  <div class="flex">
    <span class="self-end text-lg text-green-500">{{ price / 100 }}</span>
    <span class="self-start text-lg text-gray-700 ml-1">€</span>
  </div>
</template>
