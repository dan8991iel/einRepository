<template>
    <div class="flex w-full">
      <div class="mb-4">
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
        <div class="flex items-center justify-end">
          <button
            class="bg-indigo-500 text-white p-2 rounded-lg hover:bg-indigo-600"
            type="submit"
          >
            Edit Product
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
const products: Product[] = [
    {
    id: 1,
    name: "Product 1",
    price: 9.99,
    description: "This is a sample product",
    category_name: "Category 1",
    image_url: ""
    },
    {
    id: 2,
    name: "Product 2",
    price: 9.99,
    description: "This is a sample product",
    category_name: "Category 1",
    image_url: ""
    },
    {
    id: 3,
    name: "Product 3",
    price: 9.99,
    description: "This is a sample product",
    category_name: "Category 1",
    image_url: ""
    }
];



function editProduct() {
    console.log("Edited Product: ", selectedProduct.value);
}

</script>