<script setup lang="ts">
import type { CartItem } from '@/models/CartItem';
import { useCartStore } from '@/stores/cart';
import { ref, watch } from 'vue';
import PriceDisplay from './PriceDisplay.vue';

const props = defineProps<{
  item: CartItem,
}>();

const cart = useCartStore();

let count = ref(props.item.count);
watch(props, (props) => count.value = props.item.count);
watch(count, (count) => cart.setCount(props.item.product, count));
</script>

<template>
  <div class="flex items-center py-4 border-b border-gray-200">
    <div class="w-20 bg-cover rounded-lg aspect-square"
      :style="{ backgroundImage: `url('${item.product.image_url}')` }"></div>
    <div class="flex-1 mx-6">
      <h3 class="font-bold text-md">{{ item.product.name }}</h3>
      <h4 class="mt-1 text-sm text-green-500">Auf Lager</h4>
      <h4 class="mt-1 text-sm text-gray-800">Stückpreis: {{ item.product.price }}</h4>
    </div>
    <div>
      <h5 class="mb-1 ml-2 text-sm text-gray-600">Anzahl</h5>
      <div class="flex items-center">
        <input v-model="count" min="1" max="99" type="number"
          class="w-24 p-2 font-medium border border-gray-400 rounded-lg" />
        <mdicon name="trash-can" @click="cart.removeAllOfProduct(item.product)"
          class="ml-2 text-gray-500 cursor-pointer hover:text-red-500" />
      </div>
    </div>
    <div class="ml-12 text-right">
      <h5 class="mb-1 text-sm text-gray-600">Preis</h5>
      <div class="h-[42px] items-center flex">
        <PriceDisplay :price="item.totalPrice"></PriceDisplay>
      </div>
    </div>
  </div>
</template>