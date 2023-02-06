<style>
    .inputSection{
        background-color: lightgray;
        pointer-events: none;
    } 

</style>

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
          @change="updateForm"
        >
          <option v-for="product in products" :value="product">{{ product.name }}</option>
        </select>
      </div>


      <form @submit.prevent="editProduct" id="edit-form" class="w-full p-6 bg-white rounded-lg">
        <div class="mb-4">
          <label class="block mb-2 font-medium text-gray-700" for="name">
            Name:
          </label>
          <input
            class="inputSection w-full p-2 border border-gray-400 rounded-lg disabled:bg-gray-300 disabled:pointer-events-none"
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
            class="w-full p-2 border border-gray-400 rounded-lg inputSection"
            v-model="selectedProduct.price"
            type="number"
            step="any"
            id="price"
            required
          />
        </div>
        <div class="mb-4">
          <label class="block mb-2 font-medium text-gray-700" for="description">
            Description:
          </label>
          <textarea
            class="w-full p-2 border border-gray-400 rounded-lg inputSection"
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
            class="w-full p-2 border border-gray-400 rounded-lg inputSection"
            v-model="selectedProduct.category_name"
            type="text"
            id="category"
            required
          />
        </div>
        <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="image"
          >Image:</label
        >
        <ImageUpload  v-model:image-url="selectedProduct.image_url" />
        </div>
        <div class="flex items-center justify-start">
            <button
            id ="submit-button"
            class="px-4 py-2 text-white enabled:bg-green-500 rounded-lg enabled:hover:bg-green-600 disabled:bg-green-900 disabled:pointer-events-none"
            type="submit"
            disabled
            >
                Save Changes
            </button>
        </div>
      </form>
    </div>
</template>


<script setup lang="ts">
import { ref, type ButtonHTMLAttributes, type FormHTMLAttributes, type HTMLAttributes } from "vue";
import type { Ref } from "vue";
import type { Product } from "@/models/Product";
import ImageUpload from "./ImageUpload.vue";


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

  const emptySlot : Product = {id:0,name:'----CLEAR----',price:0,description:'',category_name:'',image_url:''};
  products.value.unshift(emptySlot);
}

await getproducts();

function updateForm() {
    console.log("Edited Product: ", selectedProduct.value);
    let elements = document.getElementsByClassName('inputSection') as HTMLCollectionOf<HTMLElement>;
    let button = document.getElementById('submit-button') as HTMLInputElement | null;

    if(selectedProduct.value.id === 0){ 
        for(let element of elements){
            element.setAttribute("style", "background-color: lightgray;pointer-events: none;");
        }
        button?.setAttribute("disabled", "");
    }
    else{
        for(let element of elements){
            element.setAttribute("style", "background-color: white;pointer-events: all;");
        }
        button?.removeAttribute('disabled')
    }
}


function editProduct() {
    console.log("Edited Product: ", selectedProduct.value);
}

</script>