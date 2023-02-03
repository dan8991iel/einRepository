<script setup lang="ts">
import { useCartStore } from "@/stores/cart";
import { RouterLink } from "vue-router";
import Popper from "vue3-popper";
import ShoppingCartCount from "./ShoppingCartCount.vue";

const cart = useCartStore();
</script>

<template>
  <div>
    <Popper content="Warenkorb" :hover="true" :arrow="true" style="display: block">
      <RouterLink to="/cart" class="block p-2">
        <div class="relative block">
          <mdicon :name="cart.productCount > 0 ? 'cart' : 'cart-outline'" size="32"
            class="text-gray-600 hover:text-gray-900 active:text-black" />
          <ShoppingCartCount v-if="cart.itemCount > 0" :item-count="cart.itemCount" />
        </div>
      </RouterLink>
    </Popper>
  </div>
</template>
