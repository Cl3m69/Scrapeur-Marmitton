const ScrapeurMarmiton = require("./Scrapeur/ScrapMarmiton");
const CreateCSV = require("./Scrapeur/Papaparse");

(async () => {
    await ScrapeurMarmiton.getIdRecette();
    for (var i = 0; i < ScrapeurMarmiton.arrayIdRecette.length; i++)
        await ScrapeurMarmiton.recupRecetteMarmiton(ScrapeurMarmiton.arrayIdRecette[i]);
    await CreateCSV.convertJSONToCSV(ScrapeurMarmiton.dataJSON);
})();
