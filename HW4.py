#Name: Preston
#Class: 5th Hour
#Assignment: HW4

print("Hello World!")

albumsDict = {
 "artist" : "David Bowie",
 "album"  : "Station to Station",
 "year"   : "1976",
}
print(albumsDict)
print(albumsDict["artist"])
print(albumsDict["year"])

albumsDict.update({"number of songs": 6})

print(albumsDict)

albumsDict.clear()
print(albumsDict)

favoriteArtists = {
 "artist1": {
  "name" : "David Bowie",
  "genre": "Rock",
  "favorite album": "Station to Station",
 },
 "artist2": {
  "name" : "The Strokes",
  "genre": "Rock",
  "favorite album": "Is This It",
 }
},

print(favoriteArtists)

print(favoriteArtists["artist1"])
