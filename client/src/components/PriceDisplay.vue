<script setup lang="ts">
defineProps<{
  price: number;
}>();
</script>

<template>
  <div class="self-center text-green-500">
    <span class="text-xl">{{ Math.floor(price / 100) }},</span>
    <span class="text-sm relative -top-[5px]">{{ price % 100 }}</span>
  </div>
</template>
