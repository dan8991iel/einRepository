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
 
    await page.waitForTimeout(400)

  await page.goto('http://localhost:5173/');
  //await page.waitForTimeout(400)
  //await page.screenshot({path: 'test.png'});

  // Expect a title "to contain" a substring.
  await expect(page.locator("h1").last()).toHaveText(/Keks/);
  //await expect(page).toHave(/Keks/);
});

test('get started link', async ({ page }) => {
  await page.goto('https://playwright.dev/');

  // Click the get started link.
  await page.getByRole('link', { name: 'Get started' }).click();

  // Expects the URL to contain intro.
  await expect(page).toHaveURL(/.*intro/);
});
function db_connection() {
  throw new Error('Function not implemented.');
}

