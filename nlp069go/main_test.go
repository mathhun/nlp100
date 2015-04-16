package main_test

import (
	"testing"
	. "github.com/smartystreets/goconvey/convey"
	"net/http"
	"io/ioutil"
	"encoding/json"
)

type SearchResultJson struct {
	Name string
}

func TestSpec(t *testing.T) {
	Convey("When searching with an artist name", t, func () {
		resp, _ := http.Get("http://localhost:3001/artists?name=Oasis")
		body, _ := ioutil.ReadAll(resp.Body)

		var result []SearchResultJson
		json.Unmarshal(body, &result)

		Convey("Response code should be 200", func () {
			So(resp.StatusCode, ShouldEqual, 200)
		})

		Convey("Response should be JSON Array", func () {
			So(string(body), ShouldStartWith, "[")
			So(string(body), ShouldEndWith, "]")
		})

		Convey("Response should contain the artist name", func () {
			So(result[0].Name, ShouldEqual, "Oasis")
		})

		Convey("Response should contain 3 records", func () {
			So(len(result), ShouldEqual, 3)
		})
	})
}
