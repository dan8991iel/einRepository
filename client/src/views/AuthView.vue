<script setup lang="ts">
import { EmailAuthProvider } from "firebase/auth";
import * as firebaseui from "firebaseui";
import { onMounted, onUnmounted } from "vue";
import { useFirebaseAuth } from "vuefire";

const firebaseAuth = useFirebaseAuth();

let ui: firebaseui.auth.AuthUI;

onMounted(() => {
  const uiConfig = {
    signInSuccessUrl: "/",
    signInOptions: [EmailAuthProvider.PROVIDER_ID],
  };
  ui = new firebaseui.auth.AuthUI(firebaseAuth);
  ui.start("#firebaseui-auth-container", uiConfig);
});

onUnmounted(() => {
  ui.delete();
});
</script>

<template>
  <div id="firebaseui-auth-container" class="my-12"></div>
</template>
