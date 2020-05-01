# API Documentation

our API has several endpoints. 

`GET` - `/users`

> get all users from db. No authorisation needed.

---

`GET` - `/districts`
> Get all the dsitricts. No authrisation needed.

```json
[
	castel: {
		count: 5,
		type: "noble",
		cost: 4,
		extra: ""
	},
	museum: {
		count: 1,
		type: "unique",
		cost: 2,
		extra: "When musem gets build it can be build by any gold and is worth of double the amount"
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
> get all the cahracters.No authrisation needed.

```json
[
	assasin: {
		orderNumber: 1,
		power: "Kill acharcter"
	}, 
	thief: {
		orderNumber: 2,
		power: "Choose a character to steal money from"
	},
	magicion: {
		orderNumber: 3,
		power: "chooses a character to swap hands with"
	}
]
```

---

`POST` - `/users`

> create a new user in the database.no authorisation needed. It return a token as a response that contains information about the username. body:

```json
{
	username: "monkey",
	email: "mon@mon.com",
	password: "123"
}
```

---

`POST` - `/login`

> login in your account. the response return a JWT token. body:

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
			districtsInHand: ["trade mill", "castel", "museum", "statue"],
			goldCount: 2,
			districtsBuilt: [],
			characterRole: "",
			totalPoints: 0
		}}
	]
}
```

`PUT` - `/games?fac19`

> join the game named fac19 after getting the link from game creator. Authorisation needed. No response pody requred. The playerUsernames will automatically get updated.
---

`GET` - `/games/fac19`

> get the global state of the game bofore game starts.

```json
{
	name: "fac19",
	playerCount: "8",
	mode: "original",
	playerUsernames: [
		{monkey: {
			districtsInHand: ["fortress", "castel", "museum", "graveyeard"],
			goldCount: 2,
			districtsBuilt: [],
			characterRole: "",
			totalPoints: 0
		}},
		{ivo: {
			districtsInHand: ["jail", "castel", "church", "statue"],
			goldCount: 2,
			districtsBuilt: [],
			characterRole: "",
			totalPoints: 0
		}},
		{ako: {
			districtsInHand: ["trade mill", "castel", "museum", "statue"],
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

# tentative schema

paste this content into https://ondras.zarovi.cz/sql/demo/

If you make changes, you have to update the xml below

```xml
<sql>
<datatypes db="mysql">
	<group label="Numeric" color="rgb(238,238,170)">
		<type label="Integer" length="0" sql="INTEGER" quote=""/>
	 	<type label="TINYINT" length="0" sql="TINYINT" quote=""/>
	 	<type label="SMALLINT" length="0" sql="SMALLINT" quote=""/>
	 	<type label="MEDIUMINT" length="0" sql="MEDIUMINT" quote=""/>
	 	<type label="INT" length="0" sql="INT" quote=""/>
		<type label="BIGINT" length="0" sql="BIGINT" quote=""/>
		<type label="Decimal" length="1" sql="DECIMAL" re="DEC" quote=""/>
		<type label="Single precision" length="0" sql="FLOAT" quote=""/>
		<type label="Double precision" length="0" sql="DOUBLE" re="DOUBLE" quote=""/>
	</group>

	<group label="Character" color="rgb(255,200,200)">
		<type label="Char" length="1" sql="CHAR" quote="'"/>
		<type label="Varchar" length="1" sql="VARCHAR" quote="'"/>
		<type label="Text" length="0" sql="MEDIUMTEXT" re="TEXT" quote="'"/>
		<type label="Binary" length="1" sql="BINARY" quote="'"/>
		<type label="Varbinary" length="1" sql="VARBINARY" quote="'"/>
		<type label="BLOB" length="0" sql="BLOB" re="BLOB" quote="'"/>
	</group>

	<group label="Date &amp; Time" color="rgb(200,255,200)">
		<type label="Date" length="0" sql="DATE" quote="'"/>
		<type label="Time" length="0" sql="TIME" quote="'"/>
		<type label="Datetime" length="0" sql="DATETIME" quote="'"/>
		<type label="Year" length="0" sql="YEAR" quote=""/>
		<type label="Timestamp" length="0" sql="TIMESTAMP" quote="'"/>
	</group>
	
	<group label="Miscellaneous" color="rgb(200,200,255)">
		<type label="ENUM" length="1" sql="ENUM" quote=""/>
		<type label="SET" length="1" sql="SET" quote=""/>
		<type label="Bit" length="0" sql="bit" quote=""/>
	</group>
</datatypes><table x="292" y="71" name="users">
<row name="id" null="1" autoincrement="1">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="username" null="0" autoincrement="0">
<datatype>VARCHAR(255)</datatype>
<default>'NULL'</default></row>
<row name="email" null="0" autoincrement="0">
<datatype>VARCHAR(255)</datatype>
<default>'NULL'</default></row>
<row name="password" null="0" autoincrement="0">
<datatype>VARCHAR</datatype>
<default>'NULL'</default></row>
<key type="PRIMARY" name="">
<part>id</part>
</key>
</table>
<table x="594" y="45" name="games">
<row name="id" null="1" autoincrement="1">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="game_name" null="0" autoincrement="0">
<datatype>VARCHAR(255)</datatype>
</row>
<row name="turn_number" null="0" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="player_count" null="0" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<key type="PRIMARY" name="">
<part>id</part>
</key>
</table>
<table x="378" y="282" name="in-game-plaers">
<row name="id" null="1" autoincrement="1">
<datatype>INTEGER</datatype>
<default>NULL</default><relation table="player-districts" row="id" />
</row>
<row name="id_users" null="1" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default><relation table="users" row="id" />
</row>
<row name="id_games" null="1" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default><relation table="games" row="id" />
</row>
<row name="character_role" null="1" autoincrement="0">
<datatype>VARCHAR</datatype>
<default>NULL</default></row>
<row name="gold_count" null="0" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<key type="PRIMARY" name="">
</key>
</table>
<table x="705" y="310" name="player-districts">
<row name="id" null="1" autoincrement="1">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="ingame_player_id" null="0" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="dist1" null="1" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="dist2" null="1" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="dis3" null="1" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="..." null="1" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<key type="PRIMARY" name="">
<part>id</part>
</key>
</table>
<table x="1047" y="532" name="dsitricts">
<row name="id" null="1" autoincrement="1">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="cost" null="1" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="type" null="1" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<key type="PRIMARY" name="">
<part>id</part>
</key>
</table>
<table x="879" y="45" name="current_deck_districts">
<row name="id_games" null="1" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default><relation table="games" row="id" />
</row>
<row name="dist1" null="0" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<row name="dist2" null="0" autoincrement="0">
<datatype>INTEGER</datatype>
<default>NULL</default></row>
<key type="PRIMARY" name="">
</key>
</table>
</sql>
```
