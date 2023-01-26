<script setup lang="ts">
import PriceDisplay from "./PriceDisplay.vue";
import type { Product } from "@/models/Product";

defineProps<{
  product: Product;
}>();
</script>

<template>
  <div class="w-full max-w-sm m-4 overflow-hidden bg-white rounded-lg shadow-lg md:w-1/2 lg:w-1/3">
    <img :src="product.image_url" width="600" height="300" :alt="product.name" />
    <h3 class="mx-4 mt-4 font-semibold text-green-500 uppercase text-md">{{ product.category_name }}</h3>
    <div class="flex mx-4 mt-1 mb-2">
      <h1 class="flex-1 text-xl font-bold text-black">{{ product.name }}</h1>
      <PriceDisplay :price="product.price" class="ml-4 text-right" />
    </div>
    <p class="mx-4 mt-2 mb-4 text-gray-600">{{ product.description }}</p>
  </div>
</template>
