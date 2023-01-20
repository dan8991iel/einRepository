<script setup lang="ts">
import PriceDisplay from "./PriceDisplay.vue";
import type { Product } from "@/models/Product";

defineProps<{
  product: Product;
}>();
</script>

<template>
  <div
    class="bg-white rounded-lg shadow-lg max-w-sm w-full md:w-1/2 lg:w-1/3 m-4 overflow-hidden"
  >
    <img
      :src="`https://source.unsplash.com/random/600x300?${image()}`"
      width="600"
      height="300"
      :alt="product.name"
    />
    <div class="flex mx-4 mt-4 mb-2">
      <h1 class="text-xl font-bold text-black flex-1">{{ product.name }}</h1>
      <PriceDisplay :price="product.price" class="ml-4 text-right" />
    </div>
    <p class="mx-4 mt-2 mb-4 text-gray-600">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
      tempor incididunt ut labore et dolore magna aliqua. Eget aliquet nibh
      praesent tristique magna. At elementum eu facilisis sed odio.
    </p>
  </div>
</template>

<script lang="ts">
const imagesNames = [
  "cookie",
  "cookies",
  "cookie monster",
  "cookie jar",
  "cookie and cream",
  "chocolate cookie",
];
const image = () => imagesNames[Math.floor(Math.random() * imagesNames.length)];
</script>
