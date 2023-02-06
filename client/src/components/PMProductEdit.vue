<template>
    <div class="flex w-full">
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="select_product"
          >Select Product:</label
        >
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
          <label class="block mb-2 font-medium text-gray-700" for="name"
            >Name:</label
          >
          <input
            class="w-full p-2 border border-gray-400 rounded-lg"
            v-model="selectedProduct.name"
            type="text"
            id="name"
            required
          />
        </div>
        <div class="mb-4">
          <label class="block mb-2 font-medium text-gray-700" for="description">Description:</label>
<textarea
       class="w-full p-2 border border-gray-400 rounded-lg"
       v-model="selectedProduct.description"
       id="description"
       required
     ></textarea>
</div>
<div class="mb-4">
<label class="block mb-2 font-medium text-gray-700" for="price"
       >Price:</label
     >
<input
       class="w-full p-2 border border-gray-400 rounded-lg"
       v-model="selectedProduct.price"
       type="number"
       id="price"
       required
     />
</div>
<div class="mb-4">
<label class="block mb-2 font-medium text-gray-700" for="stock"
       >Stock:</label
     >
<input
       class="w-full p-2 border border-gray-400 rounded-lg"
       v-model="selectedProduct.stock"
       type="number"
       id="stock"
       required
     />
</div>
<div class="mb-4">
<label class="block mb-2 font-medium text-gray-700" for="category"
       >Category:</label
     >
<input
       class="w-full p-2 border border-gray-400 rounded-lg"
       v-model="selectedProduct.category"
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
<script>
export default {
  data() {
    return {
      selectedProduct: {},
      products: [
        {
          id: 1,
          name: "Product 1",
          description: "This is a sample product",
          price: 9.99,
          stock: 10,
          category: "Category 1"
        },
        {
          id: 2,
          name: "Product 2",
          description: "This is another sample product",
          price: 19.99,
          stock: 20,
          category: "Category 2"
        },
        {
          id: 3,
          name: "Product 3",
          description: "This is yet another sample product",
          price: 29.99,
          stock: 30,
          category: "Category 3"
        }
      ]
    };
  },
  methods: {
    editProduct() {
      // Add logic for editing product
      console.log("Edited Product: ", this.selectedProduct);
    }
  }
};
</script>