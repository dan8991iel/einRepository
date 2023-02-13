<style></style>

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
        <option :key="product.id" v-for="product in products" :value="product">
          {{ product.name }}
        </option>
      </select>
    </div>

    <form
      @submit.prevent="editProduct"
      id="edit-form"
      class="w-full p-6 bg-white rounded-lg"
    >
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
          class="w-full p-2 border border-gray-400 rounded-lg inputSection disabled:bg-gray-300 disabled:pointer-events-none"
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
          class="w-full p-2 border border-gray-400 rounded-lg inputSection disabled:bg-gray-300 disabled:pointer-events-none"
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
          class="w-full p-2 border border-gray-400 rounded-lg inputSection disabled:bg-gray-300 disabled:pointer-events-none"
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
        <ImageUpload v-model:image-url="selectedProduct.image_url" />
      </div>
      <div class="flex items-center justify-start">
        <button
          id="submit-button"
          class="px-4 py-2 text-white enabled:bg-green-500 rounded-lg enabled:hover:bg-green-600 disabled:bg-green-900 disabled:pointer-events-none"
          type="submit"
          disabled
        >
          Save Changes
        </button>
        <button
          id="rest-button"
          class="px-4 py-2 mx-2 text-white enabled:bg-green-500 rounded-lg enabled:hover:bg-green-600 disabled:bg-green-900 disabled:pointer-events-none"
          @click="resetForm"
          disabled
          value="ignore"
          formnovalidate
          type="button"
        >
          Reset Form
        </button>
      </div>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import type { Ref } from "vue";
import type { Product } from "@/models/Product";
import ImageUpload from "./ImageUpload.vue";

const emptyProduct: Product = {
  id: 0,
  name: "",
  price: null,
  description: "",
  category_name: "",
  image_url: "",
};

//To reset seperate product informations
//var selectedProductTemp: Ref<Product> = ref(emptyProduct as Product);

const selectedProduct: Ref<Product> = ref(emptyProduct as Product);
const products: Ref<Product[]> = ref([]);

onMounted(() => {
  updateForm();
});

async function getproducts() {
  const result = await fetch(
    `${import.meta.env.VITE_API_PROT}://${import.meta.env.VITE_API_HOST}${
      import.meta.env.VITE_API_PATH
    }/products`
  );
  products.value = await result.json();
  console.log(products.value);

  //const emptySlot : Product = emptyProduct;
  products.value.unshift(emptyProduct);
}

await getproducts(); //.then(()=>updateForm());

function updateForm() {
  //selectedProductTemp.value = {id: selectedProduct.value.id, name: selectedProduct.value.name, price: selectedProduct.value.price, description: selectedProduct.value.description, category_name: selectedProduct.value.category_name, image_url:selectedProduct.value.image_url};
  let elements = document.getElementsByClassName(
    "inputSection"
  );
  let subButton = document.getElementById(
    "submit-button"
  ) as HTMLInputElement | null;
  let resButton = document.getElementById(
    "rest-button"
  ) as HTMLInputElement | null;

  console.log(selectedProduct.value.id);
  if (selectionEmpty()) {
    for (let element of elements) {
      element.setAttribute("disabled", "");
    }
    subButton?.setAttribute("disabled", "");
    resButton?.setAttribute("disabled", "");
  } else {
    for (let element of elements) {
      element.removeAttribute("disabled");
    }
    subButton?.removeAttribute("disabled");
    resButton?.removeAttribute("disabled");
  }
}

function editProduct() {
  const product: Product = {
    id: selectedProduct.value.id,
    name: selectedProduct.value.name,
    price: Number(selectedProduct.value.price),
    description: selectedProduct.value.description,
    image_url: selectedProduct.value.image_url,
    category_name: selectedProduct.value.category_name,
  };

  console.log(JSON.stringify(product));

  fetch(
    `${import.meta.env.VITE_API_PROT}://${import.meta.env.VITE_API_HOST}${
      import.meta.env.VITE_API_PATH
    }/products/edit`,
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

function resetForm() {
  /*if(selectionEmpty()){
        selectedProduct.value = emptyProduct;
    }else{
      selectedProduct.value = {id: selectedProductTemp.value.id, name: selectedProductTemp.value.name, price: selectedProductTemp.value.price, description: selectedProductTemp.value.description, category_name: selectedProductTemp.value.category_name, image_url:selectedProductTemp.value.image_url};
    }

    let dropDownBox : HTMLSelectElement= document.getElementById("select_product") as HTMLSelectElement;
    if(dropDownBox){
      dropDownBox.value = selectedProduct.value.name;
    }*/
  getproducts();
  selectedProduct.value = emptyProduct;
  updateForm();
}

function selectionEmpty() {
  if (
    selectedProduct.value.id === 0 ||
    selectedProduct.value.id === undefined ||
    selectedProduct.value.id === null
  ) {
    return true;
  }
  return false;
}
</script>
