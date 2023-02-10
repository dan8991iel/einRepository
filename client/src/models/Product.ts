export interface Product {
  id: number;
  name: string;
  price: number | null;
  description: string;
  category_name: string;
  image_url: string;
}

export interface NewProduct {
  name: string;
  price: number;
  description: string;
  category_name: string;
  image_url: string;
}
