<script setup lang="ts">
import { useCurrentUserRole } from '@/auth';
import Popper from "vue3-popper";
import { useCurrentUser, useFirebaseAuth } from "vuefire";

const user = useCurrentUser();
const auth = useFirebaseAuth();
const role = useCurrentUserRole();
</script>

<template>
  <div class="flex items-center ml-4">
    <Popper content="Logout" :hover="true" :arrow="true">
      <button @click="auth?.signOut()" class="h-12 cursor-pointer">
        <img :src="user?.photoURL" v-if="user?.photoURL" class="w-auto h-full rounded-full" />
        <div class="flex items-center justify-center h-full bg-gray-200 rounded-full aspect-square">
          <mdicon name="account" size="36" class="text-gray-600" />
        </div>
      </button>
    </Popper>
    <div class="ml-2">
      <h4>{{ user?.displayName }}</h4>
      <h5>{{ role }}</h5>
    </div>
  </div>
</template>
