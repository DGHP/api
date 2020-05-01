// this is basically for JSON. It's a .js file so we can have comments
// not an actual schema just for discussion of what needs to go into game objects

const game = {
	name: "fac19",
	playerCount: "8",
    mode: "original",
    characterDeck: [],
    districtDeck: [],
    turn: 0, // we can sort playerUsernames by the value of their characterRole, then use turn to look up the specific player we're interested in this turn. This could be done on the frontend, but with this information
    stage: "character-selection", // also "player-turns"
	playerUsernames: [
		{monkey: {
			districtsInHand: ["fortress", "castle", "museum", "graveyeard"],
			goldCount: 2,
			districtsBuilt: [],
			characterRole: "",
			totalPoints: 0
		}},
		{ivo: {
			districtsInHand: ["jail", "castle", "church", "statue"],
			goldCount: 2,
			districtsBuilt: [],
			characterRole: "",
			totalPoints: 0
		}},
		{ako: {
			districtsInHand: ["trade mill", "castle", "museum", "statue"],
			goldCount: 2,
			districtsBuilt: [],
			characterRole: "",
			totalPoints: 0
		}}
	]
}