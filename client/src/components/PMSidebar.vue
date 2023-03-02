<template>
  <div class="pl-4 pt-4 pb-4">
    <div class="p-4 bg-gray-200 md:min-h-screen min-w-min rounded-lg">
      <div class="mb-2 text-lg font-medium">Product Maintenance</div>
      <router-link
        class="flex-1 block w-full p-2 mb-2 text-center text-white bg-green-500 rounded-lg whitespace-nowrap"
        to="/admin/products/add"
        active-class="bg-green-600"
      >
        Add Product
      </router-link>
      <router-link
        class="flex-1 block w-full p-2 mb-2 text-center text-white bg-green-500 rounded-lg whitespace-nowrap"
        to="/admin/products/edit"
        active-class="bg-green-600"
      >
        Edit Product
      </router-link>
      <router-link
        class="flex-1 block w-full p-2 mb-2 text-center text-white bg-green-500 rounded-lg whitespace-nowrap"
        to="/admin/products/remove"
        active-class="bg-green-600"
      >
        Remove Product
      </router-link>
    </div>
  </div>
</template>
