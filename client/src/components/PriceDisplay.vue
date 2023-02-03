<script setup lang="ts">
import { computed } from "vue";

const props = defineProps<{
  price: number;
}>();

const minorUnits = computed(() => {
  const value = Math.round((props.price - Math.floor(props.price)) * 100);
  if (value < 10) {
    return `0${value}`;
  }
  return value;
});
</script>

<template>
  <div class="self-center font-bold text-green-500">
    <span class="text-xl">{{ Math.floor(price) }},</span>
    <span class="text-sm relative -top-[5px]">{{ minorUnits }}</span>
    <span class="ml-1 text-xl">€</span>
  </div>
</template>
