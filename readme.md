# DGHP api
Written in Python 3 with MongoDB, both of which need to be installed if they are not already. The default Ubuntu Python installation needs some updating. For instance, you may need to install pip3.

## Local deployment

Setup is pretty standard for a python/mongo project. On Ubuntu, follow this set of commands:

```
git clone https://github.com/DGHP/api.git
cd api
sudo systemctl start mongod
sudo systemctl status mongod (you want to see a green circle - press q to exit)
python3 -m venv venv
source venv/activate/bin
pip3 install -r requirements.txt
touch .flaskenv
```

Edit .flaskenv with editor of choice. (Note that this is for the future - currently the flaskenv that already exists is fine)

Finally,

```
flask run
```

## Routes we've written
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/5ccd582eaacd66f56982)
(02/05/20)

Routes requiring auth use a JWT provided using the Bearer standard in the authorization header. JWTs can be obtained by creating a user or logging in. 

---

### /users

##### GET /users
Auth required: no

Gets list of all users. Probably just a development route. Returns json as body. No body required for request.

Example response body:

```
[
    {
        "_id": {
            "$oid": "5eac339e2d329d400ccd0f24"
        },
        "name": "George",
        "email": "g@g.com",
        "password": "pbkdf2:sha256:150000$reMXUvhC$50b9651e8b8cf2a2de62c422efd5b1a1cf3de28b07767045f9530ea41205bed4"
    }
]
```

#### POST /users
Auth required: no

Adds user to the system and logs them in, returning a JWT as a string in the response body.

Example request body:
```
{
    "name": "Ivo",
    "password": "password"
}
```

Example response body:

```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ikl2byIsImlhdCI6MTU4ODQyMzQ3NSwiZXhwIjoxNTg5MDI4Mjc1fQ.xx6Toj-R_H4M0oulywByLs4uvYJVGDwtrTpy9fb7c14
```

---

### /login

#### POST /login
Auth required: no

Returns a JWT, in string form. Credentials should be provided in the body.

Example request body:
```
{
    "name": "Ivo",
    "password": "password"
}
```

Example response body:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Ikl2byIsImlhdCI6MTU4ODQyMzQ3NSwiZXhwIjoxNTg5MDI4Mjc1fQ.xx6Toj-R_H4M0oulywByLs4uvYJVGDwtrTpy9fb7c14
```

---

### /games

#### GET /games
Auth required: no

Gets all games, returned as array in body.

Example response body:
```
[
    {
        "_id": {
            "$oid": "5ead438bcc7eac60028f857b"
        },
        "name": "fac19",
        "playerCount": 8,
        "mode": "original",
        "characterDeck": [],
        "districtDeck": [],
        "turn": 0,
        "stage": "character-selection",
        "players": [
            {
                "Monkey": {
                    "districtsInHand": [],
                    "goldCount": 0,
                    "districtsBuilt": [],
                    "characterRole": "",
                    "totalPoints": 0
                }
            }
        ]
    }
]
```


#### POST /games
Auth required: yes

Creates a new game

Example request body:
```
{
	"name": "fac19",
	"playerCount": 8,
	"mode": "original",
	"playerUsernames": ["Monkey"]
}
```

```
new game created
```

#### PUT /games/name=\<game name\>&username=\<username\>
Auth required: yes

Adds specified user to game

No body required

This route is likely to change soon

Example url:
```
http://127.0.0.1:5000/games?name=fac19&username=ivo
```

---

## Routes we might write




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
