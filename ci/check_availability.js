const puppeteer = require("puppeteer");
const fs = require("fs");
const dir = "./ci/screenshots";
const url = "http://127.0.0.1:8001/";

if (!fs.existsSync(dir)) {
  fs.mkdirSync(dir);
}
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({
    width: 1920,
    height: 1080,
  });
  try {
    await page.goto(url);
    await page.screenshot({ path: dir + "/login.png" });
	await page.waitForSelector('#tl_login', {timeout: 60000});
    await page.tap("#tl_login");
    await page.type("#tl_login", "user");
    await page.tap("#tl_password");
    await page.type("#tl_password", "bitnami");
    await page.keyboard.press("Enter", { delay: 3000 });
    await page.screenshot({ path: dir + "/index.png" });
    //await page.tap("#input_go");
   
    await page.screenshot({ path: dir + "/notice.png" });
  } catch (e) {
    console.log(e.toString());
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
