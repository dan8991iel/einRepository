<script setup lang="ts">
import { ref } from "vue";
import CartList from "@/components/CartList.vue";
import PriceDisplay from "@/components/PriceDisplay.vue";
import { useCartStore } from "@/stores/cart";

const cart = useCartStore();

const first_name = ref("");
const last_name = ref("");
const street = ref("");
const house_number = ref("")
const plz = ref("");
const city = ref("");
const country = ref("");

  /*fetch(
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
}*/

</script>

<template>
  <main class="max-w-full mx-auto my-4 lg:my-12 lg:max-w-3xl">
    <div class="left-0 right-0 p-8 mx-4 bg-white rounded-lg">
      <h1 class="mb-4 text-4xl font-black">Bestellübersicht</h1>

      <h2 class="mb-1 text-sm text-gray-600">Lieferinformationen</h2>

      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="firstname"
          >Firstname:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="first_name"
          type="string"
          id="firstname"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="lastname"
          >Lastname:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="last_name"
          type="string"
          id="lastname"
        />
      </div>
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="street"
          >Street:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="street"
          type="string"
          id="street"
          required
        />
        <label class="block mb-2 font-medium text-gray-700" for="housenumber"
          >Housenumber:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="house_number"
          type="string"
          id="housenumber"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="plz"
          >PLZ:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="plz"
          type="string"
          id="plz"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="city"
          >City:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="city"
          type="string"
          id="city"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block mb-2 font-medium text-gray-700" for="country"
          >Country:</label
        >
        <input
          class="w-full p-2 border border-gray-400 rounded-lg"
          v-model="country"
          type="string"
          id="country"
          required
        />
      </div>

      <h2 class="mb-1 text-sm text-gray-600">Bezahlung über:</h2>
      <div class="text-right">
          <h3 class="mb-1 text-sm text-gray-600">Gesamtpreis</h3>
          <PriceDisplay :price="cart.totalPrice" class="mb-1" />
          <h4 class="text-xs text-gray-600">inkl. Mwst., zzgl. Versand</h4>
        </div>
      </div>

      <div class="flex justify-end w-full mt-4" v-if="cart.itemCount > 0">
        <div class="text-right">
          <button class="inline-block px-4 py-2 mt-4 font-bold text-white transition-shadow bg-green-500 rounded-lg hover:shadow-lg active:bg-green-600"><RouterLink to="/closingorders">
        <div class="text-center">
          <h3>Jetzt Bestellen</h3>
        </div>
      </RouterLink></button>
      </div>
    </div>
  </main>
</template>
