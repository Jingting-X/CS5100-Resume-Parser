const webdriver = require('selenium-webdriver');
const {By, Key, Builder, WebElement} = require("selenium-webdriver");
require("chromedriver")

async function example(){
    let driver = await new Builder().forBrowser("chrome").build();
    //Local url of the web app
    await driver.get("http://localhost:63343/frontend/index.html?_ijt=49lsc781udoqeh7sb2g635bc9g");

    //Title test
    const title = await driver.getTitle();

    console.log('Title is', title);

    //Button test
    let button = driver.findElement(By.id("updateButton"));
    let check = button.isSelected();
    if (check){
        console.log("Button has been clicked")
    } else {
        console.log("Click the upload button");
        button.click();
    }

    //Upload file test
    let file = driver.findElement(By.id("file"));
    //pick a file locally, and automated submit
    await file.sendKeys("/Users/jinyinchai/Desktop/about_me.txt");
    let text = await driver.findElement(By.id("filechosen")).getText();

    console.log("Upload File Test:" + text);

}

example();

