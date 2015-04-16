package main

import (
	"github.com/go-martini/martini"
	"gopkg.in/mgo.v2"
	"gopkg.in/mgo.v2/bson"
	"encoding/json"
	"net/http"
	"log"
)

//[{'rating': {'count': '13', 'value': '86'}, 'aliases': ['OASIS', 'オアシス'], 'area': 'United Kingdom', 'name': 'Oasis', 'tags': ['rock', 'britpop', 'british', 'uk', 'britannique', 'rock and indie', 'england', 'manchester']}, {'rating': {'count': 'NA', 'value': 'NA'}, 'aliases': [], 'area': 'United Kingdom', 'name': 'Oasis', 'tags': ['morning glory', 'oasis']}, {'rating': {'count': 'NA', 'value': 'NA'}, 'aliases': [], 'area': 'United States', 'name': 'Oasis', 'tags': []}]

func main() {
	app := NewMyApp()
	app.m.Get("/artists", app.GetArtists)
	app.m.Run()
}

func (app *MyApp) GetArtists(r *http.Request) (int, []byte) {
	qs := r.URL.Query()
	name, alias, tag := qs.Get("name"), qs.Get("alias"), qs.Get("tag")

	c := SearchCriteria{name, alias, tag}
	res := app.Search(&c)

	bs, err := json.Marshal(res)
	if err != nil {
		log.Fatal(err)
		return 500, []byte("ERROR")
	}

	if len(bs) == 4 && string(bs) == "null" {
		bs = []byte("[]")
	}

	return 200, bs
}

type SearchCriteria struct {
	Name string
	Alias string
	Tag string
}

type SearchResult struct {
	Name string
	Aliases []map[string]interface{}
	Tags []map[string]interface{}
}

type MyApp struct {
	m *martini.ClassicMartini
	db *mgo.Collection
}

func NewMyApp() MyApp {
	var app MyApp
	app.m = martini.Classic()
	app.ConnectDB()
	return app
}

func (app *MyApp) ConnectDB() {
	session, err := mgo.Dial("localhost")
	if err != nil {
		panic(err)
	}

	c := session.DB("nlp").C("artists")

	app.db = c
}

func (app *MyApp) Search(s *SearchCriteria) []SearchResult {
	var r []SearchResult

	q := bson.M{}
	if len(s.Name) > 0 {
		q["name"] = s.Name
	}
	if len(s.Alias) > 0 {
		q["aliases.name"] = s.Alias
	}
	if len(s.Tag) > 0 {
		q["tags.value"] = s.Tag
	}

	err := app.db.Find(q).All(&r)
	if err != nil {
		log.Fatal(err)
	}

	return r
}
