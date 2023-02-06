import CartView from "@/views/CartView.vue";
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/cart",
      name: "cart",
      component: CartView,
    },
    {
      path: "/contact",
      name: "contact",
      component: () => import("../views/ContactView.vue"),
    },
    {
      path: "/auth",
      name: "auth",
      component: () => import("../views/AuthView.vue"),
    },
    {
      path: "/admin/products",
      name: "ProductMaintenance",
      component: () => import("../views/ProductMaintenanceView.vue"),
      children: [
        {
          path: "add",
          name: "product-add",
          component: () => import("../views/admin/AddProductView.vue"),
        },
        {
          path: "edit",
          name: "product-edit",
          component: () => import("../views/admin/EditProductView.vue"),
        },
        {
          path: "remove",
          name: "product-remove",
          component: () => import("../views/admin/AddProductView.vue"),
        },
      ],
    },
  ],
});

export default router;
