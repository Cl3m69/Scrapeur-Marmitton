const Papa = require("papaparse");
var fs = require("fs");

const createCSV = {
    writeFile: (data) => {
        fs.writeFile("recettes.csv", data, { flag: "a" }, function (err, dat) {
            console.log(err);
        });
        return;
    },

    createFile: async (data) => {
        fs.readFile("recettes.csv", function (err, dat) {
            if (err !== null) fs.createWriteStream("recettes.csv");
            createCSV.writeFile(data);
        });
        return;
    },

    convertJSONToCSV: async (dataJSON) => {
        for (var i = 0; i < dataJSON.length; i++) {
            var step = dataJSON[i].etapes;
            var stepString = "";
            step.map((elem, index) => {
                if (step.length === index + 1) stepString = stepString + elem;
                else stepString = stepString + elem + " || ";
            });
            dataJSON[i].etapes = stepString;
            var ingredients = dataJSON[i].ingredients;
            var ingredientsString = "";
            ingredients.map((elem, index) => {
                if (elem.name) ingredientsString = ingredientsString + elem.name;
                else ingredientsString = ingredientsString + "null";
                if (elem.quantity) ingredientsString = ingredientsString + " " + elem.quantity;
                if (elem.unitName) ingredientsString = ingredientsString + " " + elem.unitName;
                if (ingredients.length !== index + 1)
                    ingredientsString = ingredientsString + " || ";
            });
            dataJSON[i].ingredients = ingredientsString;
        }
        var csv = Papa.unparse(dataJSON, {
            quotes: true,
            quoteChar: '"',
            escapeChar: '"',
            delimiter: ",",
            header: true,
            newline: "\r\n",
        });
        createCSV.createFile(csv);
        return;
    },
};

module.exports = createCSV;
