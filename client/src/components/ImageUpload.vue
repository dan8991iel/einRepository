<script setup lang="ts">
import { uuidv4 } from "@firebase/util";
import { useFileDialog } from "@vueuse/core";
import { ref as storageRef } from "firebase/storage";
import { ref, watchEffect } from "vue";
import { useFirebaseStorage, useStorageFile } from "vuefire";

const storage = useFirebaseStorage();
const uploadedFileRef = storageRef(storage, `images/${uuidv4()}.jpg`);
const hasUploaded = ref<boolean>(false);

defineProps(["imageUrl"]);
const emit = defineEmits<{
  (e: "update:imageUrl", imageUrl: string | null): void;
}>();

const { url, uploadTask, upload } = useStorageFile(uploadedFileRef);

async function uploadPicture() {
  const data = files.value?.item(0);
  if (data) {
    await upload(data);
    hasUploaded.value = true;
  }
}

const { files, open } = useFileDialog();

watchEffect(() => {
  if (!hasUploaded.value && files.value?.length == 1) {
    uploadPicture();
  }
});

watchEffect(() => {
  emit("update:imageUrl", url.value ?? null);
});
</script>

<template>
  <div class="flex">
    <button
      class="inputSection self-start w-full p-2 border border-gray-400 rounded-lg enabled:hover:bg-gray-100 disabled:bg-gray-300 disabled:pointer-events-none"
      type="button"
      @click="
        open({ accept: 'image/*', multiple: false });
        hasUploaded = false;
      "
      :disabled="!!uploadTask"
    >
      <template v-if="files?.length === 1">
        Selected file: {{ files.item(0)!.name }} (Click to select another)
      </template>
      <template v-else> Select one picture </template>
    </button>

    <img
      :src="imageUrl"
      v-if="!!imageUrl"
      class="w-1/2 ml-4 rounded-lg max-w-40"
    />
  </div>
</template>
