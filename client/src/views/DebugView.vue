<script setup lang="ts">
import { computedAsync } from '@vueuse/core';
import { useCurrentUser } from 'vuefire';

const user = useCurrentUser();
const tokenContent = computedAsync(() => user.value?.getIdTokenResult());
const token = computedAsync(() => user.value?.getIdToken());
</script>

<template>
  <pre>{{ tokenContent }}</pre>

  <br />

  <label>
    Token:
  </label>
  <div>
    <textarea v-model="token"></textarea>
  </div>
</template>