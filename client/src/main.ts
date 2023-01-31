import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import mdiVue from 'mdi-vue/v3'
import * as mdijs from '@mdi/js'

import "./assets/main.css";
import { VueFire } from 'vuefire';
import { firebaseApp } from './firebase';

const app = createApp(App);

app.use(VueFire, {
  firebaseApp,
  modules: [],
})
app.use(createPinia());
app.use(router);
app.use(mdiVue, { icons: mdijs });

app.mount("#app");
