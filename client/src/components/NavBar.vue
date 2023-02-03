<script setup lang="ts">
import { useCurrentUser } from "vuefire";
import "firebaseui/dist/firebaseui.css";
import AccountNavbarIcon from "./AccountNavbarIcon.vue";
import LoginNavbarIcon from "./LoginNavbarIcon.vue";
import ShoppingCartNavbarIcon from "./ShoppingCartNavbarIcon.vue";

const user = useCurrentUser();
</script>

<template>
  <nav
    class="fixed top-0 left-0 right-0 z-50 grid w-full h-20 grid-cols-3 grid-rows-1 px-4 bg-white shadow-md lg:px-12">
    <div class="flex items-center justify-center w-full h-full col-start-2 py-4">
      <RouterLink to="/">
        <div class="text-center">
          <h1 class="text-xl text-green-500">Cookie-free Shop</h1>
          <div class="hidden text-sm text-gray-500 lg:block">
            We don't have cookies. Pinky promise!
          </div>
        </div>
      </RouterLink>
    </div>

    <div class="flex items-center justify-end col-start-3">
      <ShoppingCartNavbarIcon />

      <LoginNavbarIcon v-if="!user" class="self-center" />
      <AccountNavbarIcon v-if="!!user" />
    </div>
  </nav>
</template>
