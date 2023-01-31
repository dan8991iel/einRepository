<script setup lang="ts">
import { useCartStore } from '@/stores/cart';
import ShoppingCartCount from './ShoppingCartCount.vue';

const cart = useCartStore();
</script>

<template>
  <nav class="fixed top-0 left-0 right-0 grid w-full h-20 grid-cols-3 p-4 bg-white shadow-md lg:px-12">
    <div class="col-start-2">
      <router-link to="/">
        <div class="text-center">
          <h1 class="text-xl text-green-500">Cookie-free Shop</h1>
          <div class="text-sm text-gray-500">
            We don't have cookies. Pinky promise!
          </div>
        </div>
      </router-link>
    </div>

    <div class="flex items-center justify-end col-start-3">
      <router-link to="/cart">
        <div class="relative block">
          <mdicon :name="cart.productCount > 0 ? 'cart' : 'cart-outline'" size="32" />
          <ShoppingCartCount v-if="cart.itemCount > 0" :item-count="cart.itemCount" />
        </div>
      </router-link>
    </div>
  </nav>
</template>