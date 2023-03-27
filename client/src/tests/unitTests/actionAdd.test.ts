import { CartItem } from '@/models/CartItem';
import type { Product } from '@/models/Product';
import { createPinia, setActivePinia } from 'pinia';
import {test, describe, expect, beforeEach} from 'vitest';
import {useCartStore} from '../../stores/cart';

describe("addToCart",()=>{

    beforeEach(() => {
        setActivePinia(createPinia())
      })

    test("add the Product to cart",()=>{
        
        const store = useCartStore();
        const product:Product = {id:1, name:"Keks", price:20.00, description:"Schoko", category_name:"Lebensmittel", image_url:"https://image.essen-und-trinken.de/13073754/t/ld/v3/w960/r1/-/schokokekse-adobestock-245097665.jpg"};
        store.add(product);
        expect(Array.from (store.items.values())).toContainEqual(new CartItem(product, 1));

    })

})

