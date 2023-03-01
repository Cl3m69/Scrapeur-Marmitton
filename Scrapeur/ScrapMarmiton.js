var JSSoup = require("jssoup").default;
var axios = require("axios");
var { url, nbPage, variables } = require("../config");

var MarmitonAPI = "https://api-uno.marmiton.org/recipe/";

const ScrapeurMarmiton = {
    sleep: async (Mseconde) => {
        return await new Promise((r) => setTimeout(r, Mseconde));
    },

    arrayIdRecette: [],
    dataJSON: [],

    checkPreference: (data) => {
        if (variables.nutriScore.find((elem) => elem === data.nutriScore) === undefined) {
            console.log("NutriScore => ");
            console.log(data.nutriScore);
            return false;
        }
        if (variables.prix.find((elem) => elem === data.cost.name) === undefined) {
            console.log("Prix => ");
            console.log(data.cost.name);
            return false;
        }
        if (variables.difficulty.find((elem) => elem === data.difficulty.name) === undefined) {
            console.log("Difficulty => ");
            console.log(data.difficulty.name);
            return false;
        }
        if (variables.tempsMax < data.totalTime / 60) {
            console.log("TempsMax => ");
            console.log(data.totalTime / 60);
            return false;
        }
        if (variables.scoreMini > data.rating) {
            console.log("ScoreMini  => ");
            console.log(data.rating);
            return false;
        }
        if (variables.sansGluten === true && data.isGlutenFree === false) {
            console.log("SansGluten => ");
            console.log(data.isGlutenFree);
            return false;
        }
        if (variables.sansPorc === true && data.isPorkFree === false) {
            console.log("SansPorc => ");
            console.log(data.isPorkFree);
            return false;
        }
        if (variables.sansLactose === true && data.isLactoseFree === false) {
            console.log("SansLactose => ");
            console.log(data.isLactoseFree);
            return false;
        }
        if (variables.vegan === true && data.isVegan === false) {
            console.log("Vegan => ");
            console.log(data.isVegan);
            return false;
        }
        if (variables.vegetarien === true && data.isVegetarian === false) {
            console.log("Vegetarien => ");
            console.log(data.isVegetarian);
            return false;
        }
        return true;
    },

    recupRecetteMarmiton: async (idRecette) => {
        console.log(idRecette);
        var data = await axios.get(MarmitonAPI + idRecette);
        data = data.data;
        if (ScrapeurMarmiton.checkPreference(data) === false) {
            console.log("La recette ne correspond pas à vos préférences");
            return;
        }
        var dataRecette = {
            type: data.dishType.name,
            title: data.title,
            cookingTime: data.cookingTime / 60 + " min",
            preparationTime: data.preparationTime / 60 + " min",
            reposTime: data.restTime / 60 + " min",
            totalTime: data.totalTime / 60 + " min",
            note: data.rating,
            prix: data.cost.name,
            difficulty: data.difficulty.name,
            nbPerson: data.servings.count,
            nutriScore: data.nutriScore,
            Vegetarien: data.isVegetarian,
            Vegan: data.isVegetarian,
            etapes: [],
            ingredients: [],
        };
        data.steps.map((elem) => {
            dataRecette.etapes.push(elem.text);
        });
        data.ingredientGroups[0].items.map((elem) => {
            var ingre = {
                name: elem.name,
                quantity: elem.ingredientQuantity,
                unitName: elem.unitName,
            };
            dataRecette.ingredients.push(ingre);
        });
        ScrapeurMarmiton.dataJSON.push(dataRecette);
        return;
    },

    getIdRecette: async () => {
        for (var page = 0; page < nbPage; page++) {
            var document = await axios.get(url + page);
            var soup = new JSSoup(document.data);
            var a = soup.findAll("a");
            for (var i = 0; i < a.length; i++) {
                var index = index >= 0 && a[i].attrs.href.search(".aspx");
                if (
                    index >= 0 &&
                    index != false &&
                    a[i].attrs.href.search("https://www.marmiton.org/recettes/") >= 0
                ) {
                    var word = a[i].attrs.href.split("_");
                    var id = word[2].split(".")[0];
                    ScrapeurMarmiton.arrayIdRecette.push(id);
                }
            }
        }
        return;
    },
};

module.exports = ScrapeurMarmiton;
