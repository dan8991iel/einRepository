<script setup lang="ts">
import ProductItem from "./ProductItem.vue";

defineProps(["products"]);
</script>

<template>
  <div class="flex flex-wrap justify-center">
    <ProductItem
      v-for="product in products"
      :key="product.id"
      :product="product"
    />
  </div>
</template>
