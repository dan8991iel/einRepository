<template>
  <div class="p-4 bg-gray-200 md:min-h-screen min-w-min">
    <div class="mb-2 text-lg font-medium">Product Maintenance</div>
    <router-link class="flex-1 block w-full p-2 mb-2 text-center text-white bg-blue-500 rounded-lg whitespace-nowrap"
      to="/admin/products/add" active-class="bg-blue-600">
      Add Product
    </router-link>
    <router-link class="flex-1 block w-full p-2 mb-2 text-center text-white bg-blue-500 rounded-lg whitespace-nowrap"
      to="/admin/products/edit" active-class="bg-blue-600">
      Edit Product
    </router-link>
    <router-link class="flex-1 block w-full p-2 mb-2 text-center text-white bg-blue-500 rounded-lg whitespace-nowrap"
      to="/admin/products/remove" active-class="bg-blue-600">
      Remove Product
    </router-link>
  </div>
</template>
