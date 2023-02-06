<template>
    <div class="flex flex-col w-full p-4">
      <div class="mb-4 w-full p-6 bg-white rounded-lg">
        <label class="block mb-2 font-medium text-gray-700" for="select_product">
          Select Product:
        </label>
        <select
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="selectedProduct"
          id="select_product"
        >
          <option v-for="product in products" :value="product">{{ product.name }}</option>
        </select>
      </div>


      <form @submit.prevent="editProduct" class="w-full p-6 bg-white rounded-lg">
        <div class="mb-4">
          <label class="block mb-2 font-medium text-gray-700" for="name">
            Name:
          </label>
          <input
            class="w-full p-2 border border-gray-400 rounded-lg"
            v-model="selectedProduct.name"
            type="text"
            id="name"
            required
          />
        </div>
        <div class="mb-4">
          <label class="block mb-2 font-medium text-gray-700" for="price">
            Price:
          </label>
          <input
            class="w-full p-2 border border-gray-400 rounded-lg"
            v-model="selectedProduct.price"
            type="number"
            id="price"
            required
          />
        </div>
        <div class="mb-4">
          <label class="block mb-2 font-medium text-gray-700" for="description">
            Description:
          </label>
          <textarea
            class="w-full p-2 border border-gray-400 rounded-lg"
            v-model="selectedProduct.description"
            id="description"
            required
          ></textarea>
        </div>
        <div class="mb-4">
          <label class="block mb-2 font-medium text-gray-700" for="category">
            Category:
          </label>
          <input
            class="w-full p-2 border border-gray-400 rounded-lg"
            v-model="selectedProduct.category_name"
            type="text"
            id="category"
            required
          />
        </div>
        <div class="flex items-center justify-start">
            <button
            class="px-4 py-2 text-white bg-green-500 rounded-lg hover:bg-green-600"
            type="submit"
            >
                Save Changes
            </button>
        </div>
      </form>
    </div>
</template>


<script setup lang="ts">
import { ref } from "vue";
import type { Ref } from "vue";
import type { Product } from "@/models/Product";


const selectedProduct: Ref<Product> = ref({} as Product);
const products: Ref<Product[]> = ref([]);

async function getproducts() {
  const result = await fetch(
    `${import.meta.env.VITE_API_PROT}://${import.meta.env.VITE_API_HOST}${
      import.meta.env.VITE_API_PATH
    }/products`
  );
  products.value = await result.json();
  console.log(products.value);
}

await getproducts();

function editProduct() {
    console.log("Edited Product: ", selectedProduct.value);
}

</script>