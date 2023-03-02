<script setup lang="ts">
import { useCartStore } from "@/stores/cart";

const cart = useCartStore();

</script>

<template>
    <main class="max-w-full mx-auto my-4 lg:my-12 lg:max-w-3xl">
      <div class="left-0 right-0 p-8 mx-4 bg-white rounded-lg">
        <h1 class="mb-4 text-4xl font-black">Vielen Dank für Ihre Bestellung!</h1>

        <h2 class="mb-1 text-sm text-gray-600">Ihre Bestellung ist auf den Weg zu Ihnen.</h2>
        <button class="inline-block px-4 py-2 mt-4 font-bold text-white transition-shadow bg-green-500 rounded-lg hover:shadow-lg active:bg-green-600" @click="cart.clear()"><RouterLink to="/">
          <div class="text-center">
            <h3>Weitershoppen</h3>
          </div>
        </RouterLink></button>
     </div>
    </main>
  </template>
  