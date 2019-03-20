var request = require('request');
var cheerio = require('cheerio');

var url = "https://www.utahcounty.gov/LandRecords/Property.asp?av_serial==411750010001";

request(url, function(err, response, html) {
    if (!err) {
        var $ = cherrio.load(html);
        var allItems = $('#table').children();
        var items = [];
        allItems.each(function(index)(
            items.push($('#table').children().eq(4).find("a.title").text()))
        ));

        console.log(items)
    }
});

