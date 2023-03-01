var differentRecette = ["entree", "dessert", "plat-principal", "aperitif-ou-buffet"];
const url = "https://www.marmiton.org/recettes/index/categorie/entree/";
const nbPage = 1; // 30 * 10 = 300 recettes

// Vous pouvez ajouter vos préférences:
// false = non, true = oui

// EXAMPLE =>
// const variable = {
//     vegan: false,
//     vegetarien: true,
//     sansPorc: false,
//     sansLactose: true,
//     sansGluten: true,
//     scoreMini: 4,
//     nutriScore: ["a", "b"],
//     prix: ["bon marché", "moyen"],
//     difficulty: ["très facile", "facile", "moyenne"],
//     tempsMax: 30, // En minute
// };

const variables = {
    vegan: false,
    vegetarien: false,
    sansPorc: false,
    sansLactose: false,
    sansGluten: false,
    scoreMini: 0,
    nutriScore: ["a", "b", "c", "d", "e"],
    prix: ["bon marché", "moyen", "assez cher"],
    difficulty: ["très facile", "facile", "moyenne", "difficile"],
    tempsMax: 45, // En minute
};

module.exports = { url, nbPage, variables };
