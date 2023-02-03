<script setup lang="ts">
import ProductListTile from "./ProductListTile.vue";

defineProps(["products"]);
</script>

<template>
  <div class="flex flex-wrap items-start justify-center">
    <ProductListTile
      v-for="product in products"
      :key="product.id"
      :product="product"
    />
  </div>
</template>
