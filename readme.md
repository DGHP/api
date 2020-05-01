# DGHP api
Written in Python 3 with MongoDB, both of which need to be installed if they are not already. The default Ubuntu Python installation needs some updating. For instance, you may need to install pip3.

## Local deployment

Setup is pretty standard for a python/mongo project

```
git clone https://github.com/DGHP/api.git
cd api
sudo systemctl start mongod
sudo systemctl status mongod (you want to see a green arrow)
python3 -m venv venv
source venv/activate/bin
pip3 install -r requirements.txt
touch .flaskenv
```

Edit .flaskenv with editor of choice. 

Finally,

```
flask run
```

## API Documentation

our API has several endpoints. 

`GET` - `/users`

> get all users from db. No authorisation needed.

---

`GET` - `/districts`
> Get all the dsitricts. No authorisation needed.

```json
[
	castle: {
		count: 5,
		type: "noble",
		cost: 4,
		extra: ""
	},
	museum: {
		count: 1,
		type: "unique",
		cost: 2,
		extra: "When museum gets build it can be built by any gold and is worth of double the amount" 
	},
	statue: {
		count: 1,
		type: "unique",
		cost: 5,
		extra: "You can build same districts in your city"
	}
]
```

`GET` - `/characters`
> get all the cahracters. No authorisation needed.

```json
[
	assasin: {
		orderNumber: 1,
		power: "Kill a character"
	}, 
	thief: {
		orderNumber: 2,
		power: "Choose a character to steal money from"
	},
	magician: {
		orderNumber: 3,
		power: "chooses a character to swap hands with"
	}
]
```

---

`POST` - `/users`

> create a new user in the database. No authorisation needed. It returns a token as a response that contains information about the username. body:

```json
{
	username: "monkey",
	email: "mon@mon.com",
	password: "123"
}
```

---

`POST` - `/login`

> login to your account. the response contains a JWT. body:

```json
{
	username: "monkey",
	password: "123"
}
```

---

`POST` - `/games`

> Create a new game. Authentication needed. body:

```json
{
	name: "fac19",
	playerCount: "8",
	mode: "original",
	playerUsernames: ["monkey"]
}
```

This request sends a response:

```json
{
	name: "fac19",
	playerCount: "8",
	mode: "original",
	playerUsernames: [
		{monkey: {
			districtsInHand: ["trade mill", "castle", "museum", "statue"],
			goldCount: 2,
			districtsBuilt: [],
			characterRole: "",
			totalPoints: 0
		}}
	]
}
```

`PUT` - `/games?name=fac19&username=ivo`

> join the game named fac19 after getting the link from game creator. Authorisation needed. No response body requred. The playerUsernames will automatically get updated.
---

`GET` - `/games/fac19`

> get the global state of the game before game starts.

```json
{
	name: "fac19",
	playerCount: "8",
	mode: "original",
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
```
#### game phases

* gathering resources. choose either 2 gold or a district card

`PUT` - `/games/fac19/monkey?gold&amount=2`
> Update players gold amount for a player

`PUT` - `/games/fac19/monkey?districtinhand&distname=shop`
> Update the district name held in hand for a player

* Building phase

`PUT` - `/games/fac19/monkey?districtsbuilt&distname=museum`
> Update the districts that are built for a player

`PUT` - `/games/fac19/monkey?totalpoints&amount=5`
> Update the total points for a player

#### Delete routes
`DELETE` - `/games?name=19`
> Delete the game. authorisation needed. no body required
