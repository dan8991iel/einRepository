import { defineStore } from "pinia";
import type { Product } from "@/models/Product";
import { CartItem } from "@/models/CartItem";

export const useCartStore = defineStore("cart", {
  state: (): { items: Map<number, CartItem>; order: number[] } => ({
    items: new Map(),
    order: [],
  }),
  getters: {
    sortedItems: (state) =>
      state.order.map((productId) => state.items.get(productId)!),
    productCount: (state) => state.items.size,
    itemCount: (state) =>
      Array.from(state.items.values())
        .map((item) => item.count)
        .reduce((acc, item) => acc + item, 0),
    totalPrice: (state) =>
      Array.from(state.items.values())
        .map((item) => item.totalPrice)
        .reduce((acc, item) => acc + item, 0),
  },
  actions: {
    add(product: Product, count: number = 1) {
      if (count < 1) {
        return;
      }
      if (count !== Math.round(count)) {
        return;
      }

      count = Math.min(count, 99);

      if (this.items.has(product.id)) {
        const item = this.items.get(product.id)!;
        item.count += count;
        if (item.count > 99) {
          item.count = 99;
        }
      } else {
        this.items.set(product.id, new CartItem(product, count));
        this.order.push(product.id);
      }
    },
    setCount(product: Product, count: number): void {
      if (count < 1) {
        return;
      }
      if (count !== Math.round(count)) {
        return;
      }

      count = Math.min(count, 99);

      if (this.items.has(product.id)) {
        this.items.get(product.id)!.count = count;
      } else {
        this.items.set(product.id, new CartItem(product, count));
        this.order.push(product.id);
      }
    },
    removeCount(product: Product, count: number) {
      const item = this.items.get(product.id);
      if (!item) {
        return;
      }
      if (count < 1) {
        return;
      }
      if (count !== Math.round(count)) {
        return;
      }

      item.count -= count;
      if (item.count <= 0) {
        this.items.delete(product.id);
        const orderIndex = this.order.indexOf(product.id);
        this.order.splice(orderIndex, 1);
      }
    },
    removeAllOfProduct(product: Product) {
      this.items.delete(product.id);
      const orderIndex = this.order.indexOf(product.id);
      if (orderIndex >= 0) {
        this.order.splice(orderIndex, 1);
      }
    },
    clear() {
      this.items.clear();
      this.order = [];
    },
  },
});
