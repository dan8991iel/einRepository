import { test, expect } from '@playwright/test';
import * as mariadb from 'mariadb'

test('has title', async ({ page }) => {

  const pool=mariadb.createPool({user:"test_webshop",
                      password:"test_webshop",
                      host:"sep-dev.marcelstruck.de",
                      port:49160,
                      database:"test_webshop" 
                    })
  let conn;
  try {
  
  conn = await pool.getConnection();
  } finally {
    if (conn) conn.release(); //release to pool
  }    
      
  await conn.query("truncate table product");
  const res = await conn.query("INSERT INTO product (name, price, description, image_url, category_id) "+
    "values ('Keks', 20.00, 'Schoko', 'https://image.essen-und-trinken.de/13073754/t/ld/v3/w960/r1/-/schokokekse-adobestock-245097665.jpg', 1)");
 
  await page.waitForTimeout(400);
  await page.goto('http://localhost:5173/');
  await expect(page.locator("h1").last()).toHaveText(/Keks/);
});


test('removed Product', async ({ page }) => {

  const pool=mariadb.createPool({
    user:"test_webshop",
    password:"test_webshop",
    host:"sep-dev.marcelstruck.de",
    port:49160,
    database:"test_webshop" 
  })
let conn;
try {

conn = await pool.getConnection();
} finally {
if (conn) conn.release(); //release to pool
}    

await conn.query("truncate table product");
const res = await conn.query("INSERT INTO product (name, price, description, image_url, category_id) "+
"values ('Keks', 20.00, 'Schoko', 'https://image.essen-und-trinken.de/13073754/t/ld/v3/w960/r1/-/schokokekse-adobestock-245097665.jpg', 1)");

await page.waitForTimeout(400);
await page.goto('http://localhost:5173/');
await expect(page.locator("h1").last()).toHaveText(/Keks/);

const del = await conn.query("DELETE FROM product WHERE name = 'Keks'");

await page.waitForTimeout(400);
await page.goto('http://localhost:5173/');
await expect(page.locator("h1").last()).not.toHaveText(/Keks/);

});

function db_connection() {
  throw new Error('Function not implemented.');
}

