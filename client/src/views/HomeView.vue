<script setup lang="ts">
import ProductList from "@/components/ProductList.vue";
import HeroHeader from "@/components/HeroHeader.vue";
</script>

<template>
  <main>
    <HeroHeader />
    <ProductList :products="products" />
  </main>
</template>

<script lang="ts">
const products = [
  { id: 1, name: "Kekse", price: 242 },
  { id: 2, name: "Doppelkekse", price: 342 },
  { id: 3, name: "Krümelkekse", price: 415 },
  { id: 4, name: "Leckere Kekse", price: 252 },
  { id: 5, name: "Teure Kekse", price: 762 },
  { id: 6, name: "Oreo-Kekse", price: 1971 },
];
</script>
