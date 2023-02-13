<script setup lang="ts">
import CartList from "@/components/CartList.vue";
import PriceDisplay from "@/components/PriceDisplay.vue";
import { useCartStore } from "@/stores/cart";

const cart = useCartStore();
</script>

<template>
  <main class="max-w-full mx-auto my-4 lg:my-12 lg:max-w-3xl">
    <div class="left-0 right-0 p-8 mx-4 bg-white rounded-lg">
      <h1 class="mb-4 text-4xl font-black">Warenkorb</h1>
      <div
        class="flex flex-col items-center justify-center w-full h-60"
        v-if="cart.itemCount == 0"
      >
        <mdicon name="cart-outline" class="mb-4 text-gray-600" size="42" />
        <h2 class="mb-2 text-2xl font-medium text-gray-600">
          Der Warenkorb ist leer
        </h2>
        <h3 class="w-full max-w-md text-center text-gray-600 text-md">
          Stöber durch unser vielfältiges Sortiment und mach den Warenkorb
          glücklich
        </h3>
      </div>

      <CartList :items="cart.sortedItems" v-if="cart.itemCount > 0" />

      <div class="flex justify-end w-full mt-4" v-if="cart.itemCount > 0">
        <div class="text-right">
           <h3 class="mb-1 text-sm text-gray-600">Lieferkosten</h3>
           <PriceDisplay :price="2" class="mb-1" />
          <h3 class="mb-1 text-sm text-gray-600">Gesamtpreis</h3>
          <PriceDisplay :price="cart.totalPrice + 2" class="mb-1" />
          <h4 class="text-xs text-gray-600">inkl. Mwst., zzgl. Versand</h4>
          <button class="inline-block px-4 py-2 mt-4 font-bold text-white transition-shadow bg-green-500 rounded-lg hover:shadow-lg active:bg-green-600"><RouterLink to="/ordercompletion">
        <div class="text-center">
          <h3>Jetzt Bestellen</h3>
        </div>
      </RouterLink></button>
        </div>
      </div>
    </div>
  </main>
</template>
