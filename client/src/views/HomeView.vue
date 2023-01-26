<script setup lang="ts">
import ProductList from "@/components/ProductList.vue";
import HeroHeader from "@/components/HeroHeader.vue";
import { onMounted, ref, type Ref } from '@vue/runtime-core';
import type { Product } from '@/models/Product';

onMounted(() => {
  fetchData();
});

const products: Ref<Product[]> = ref([]);

async function fetchData() {
  const result = await fetch(`${import.meta.env.VITE_API_PROT}://${import.meta.env.VITE_API_HOST}${import.meta.env.VITE_API_PATH}/products`);
  products.value = await result.json();
}
</script>

<template>
  <main>
    <HeroHeader />
    <ProductList :products="products" />
  </main>
</template>
