<script setup lang="ts">
import Popper from "vue3-popper";
</script>

<template>
  <div>
    <Popper content="Login" :hover="true" :arrow="true" style="display: block">
      <RouterLink to="/auth" class="block p-2">
        <mdicon name="login" size="32" class="text-gray-600 hover:text-gray-900 active:text-black" />
      </RouterLink>
    </Popper>
  </div>
</template>