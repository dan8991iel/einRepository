<template>
  <div class="flex w-full">
    <form @submit.prevent="addProduct" class="w-full p-6 bg-white rounded-lg">
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="name"
          >Name:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="name"
          type="text"
          id="name"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="description"
          >Description:</label
        >
        <textarea
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="description"
          id="description"
        ></textarea>
      </div>
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="price"
          >Price:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="price"
          type="number"
          step="any"
          id="price"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="category"
          >Category:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="category_name"
          type="string"
          id="category_name"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="image"
          >Image:</label
        >
        <ImageUpload v-model:image-url="image" />
      </div>
      <button
        class="px-4 py-2 text-white bg-blue-500 rounded-lg hover:bg-blue-600"
        type="submit"
      >
        Add Product
      </button>
      <button
        class="px-4 py-2 mx-2 text-white bg-blue-500 rounded-lg hover:bg-blue-600"
        @click="resetForm"
        type="reset"
      >
        Reset Form
      </button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import type { NewProduct } from "@/models/Product";
import ImageUpload from "./ImageUpload.vue";

// interface Category {
//   name: string;
// }

const name = ref("");
const description = ref("");
const price = ref("");
const image = ref("");
const category_name = ref("");
// const categories = reactive<Category[]>([])

function addProduct() {
  const product: NewProduct = {
    name: name.value,
    price: Number(price.value),
    description: description.value,
    image_url: image.value,
    category_name: category_name.value,
  };

  console.log(JSON.stringify(product));

  fetch(
    `${import.meta.env.VITE_API_PROT}://${import.meta.env.VITE_API_HOST}${
      import.meta.env.VITE_API_PATH
    }/products`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(product),
    }
  )
    .then((response: Response) => {
      if (!response.ok) {
        console.log("NOT OKAY");
        throw new Error(response.statusText);
      }
      console.log(" OKAY");
      return response.json();
    })
    .then((data: any) => {
      console.log(" DATA");
      console.log("Product added successfully", data);
    })
    .catch((error: Error) => {
      console.error("Error adding product:", error);
    });
}

// TODO: get categories from API
/*
async function getCategories() {
  try {
    const response = await fetch("/api/categories");
    const data = await response.json();
    categories.splice(0, categories.length, ...data);
  }
  catch (error) {
    console.error(error);
  }
}

function getSelectedCategory() {
  console.log(category_name.value);
}
*/

function resetForm() {
  name.value = "";
  description.value = "";
  price.value = "";
  image.value = "";
  category_name.value = "";
}
</script>
