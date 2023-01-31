<script setup lang="ts">
defineProps<{
  itemCount: number,
}>();
</script>

<template>
  <div
    class="absolute top-[-8px] right-[-8px] flex items-center justify-center w-5 h-5 text-center text-white bg-green-500 rounded-full">
    <span :class="itemCount > 99 ? 'text-[10px]' : 'text-xs'">
      {{ itemCount > 99 ? '99+' : itemCount }}
    </span>
  </div>
</template>