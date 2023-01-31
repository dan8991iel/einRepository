<script setup lang="ts">
import CartList from '@/components/CartList.vue';
import PriceDisplay from '@/components/PriceDisplay.vue';
import { useCartStore } from '@/stores/cart';

const cart = useCartStore();
</script>

<template>
  <main class="max-w-3xl p-8 mx-auto my-12 bg-white rounded-lg">
    <h1 class="mb-4 text-4xl font-black">Warenkorb</h1>
    <CartList :items="cart.sortedItems" />

    <div class="flex justify-end w-full mt-4">
      <div class="text-right">
        <h3 class="mb-1 text-sm text-gray-600">Gesamtpreis</h3>
        <PriceDisplay :price="cart.totalPrice" class="mb-1" />
        <h4 class="text-xs text-gray-600">inkl. Mwst., zzgl. Versand</h4>
      </div>
    </div>
  </main>
</template>