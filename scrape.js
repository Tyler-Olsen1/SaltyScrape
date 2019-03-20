const request = require('request');
const cheerio = require('cheerio');

request('http://www.utahcounty.gov/LandRecords/Property.asp?av_serial=411750010001', (error, response, html) => {
    if (!error && response.statusCode == 200){
        const $ = cheerio.load(html);

        const siteTable = $('.td colspan="3"');
        console.log(siteTable.text())

    }
})