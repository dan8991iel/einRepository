<script setup lang="ts">
import type { CartItem } from "@/models/CartItem";
import CartListTile from "./CartListTile.vue";

defineProps<{ items: CartItem[] }>();
</script>

<template>
  <div>
    <CartListTile v-for="item in items" :key="item.product.id" :item="item" />
  </div>
</template>
