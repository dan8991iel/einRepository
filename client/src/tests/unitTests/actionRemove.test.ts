import {useCartStore} from '../../stores/cart';
import {test, describe, expect, beforeEach} from 'vitest';
import { createPinia, setActivePinia } from 'pinia';
import type { Product } from '@/models/Product';
import { CartItem } from '@/models/CartItem';

describe("removeFromCart",()=>{

    beforeEach(() => {
        setActivePinia(createPinia())
      })

    test("remove Product From cart",()=>{
        
        const store = useCartStore();
        const product:Product = {id:1, name:"Keks", price:20.00, description:"Schoko", category_name:"Lebensmittel", image_url:"https://image.essen-und-trinken.de/13073754/t/ld/v3/w960/r1/-/schokokekse-adobestock-245097665.jpg"};
        store.add(product);
        store.removeAllOfProduct(product);
        expect(Array.from (store.items.values())).not.toContainEqual(new CartItem(product, 1));
        expect(store.items).empty;

    })

})