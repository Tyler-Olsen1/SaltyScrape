// round 1 attempt
// const request = require('request');
// const cheerio = require('cheerio');

// request('http://www.utahcounty.gov/LandRecords/Property.asp?av_serial=411750010001', (error, response, html) => {
//     if (!error && response.statusCode == 200){
//         const $ = cheerio.load(html);

//         const siteTable = $('.td colspan="3"');
//         console.log(siteTable.text())

//     }
// })

const rp = require('request-promise');
const cheerio = require('cheerio');
const Table = require('cli-table');

let properties = [];

const options = {
    url: `http://www.utahcounty.gov/LandRecords/32916/Property.asp?av_serial=411750010001`,
    json: true
}

rp(options)
    .then((data) => {
        let promises = [];
        let propertyData = [];
        for (let property of data.LandRecords){
            propertyData.push({name: property.p})
        }
    })