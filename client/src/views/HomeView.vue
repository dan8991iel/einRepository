<script setup lang="ts">
import ProductList from '@/components/ProductList.vue';
</script>

<template>
  <main>
    <ProductList :products="products" />
  </main>
</template>

<script lang="ts">
const products = [
  { id: 1, name: "Kekse", price: 242 },
  { id: 2, name: "Doppelkekse", price: 342 },
  { id: 3, name: "Krümelkekse", price: 415 },
  { id: 4, name: "Leckere Kekse", price: 252 },
  { id: 5, name: "Teure Kekse", price: 762 }
]
</script>
