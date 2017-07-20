import facebook
import requests

token = "EAACEdEose0cBAFwmkRgvapXZAxKkh8Tg2tsjUOkn9xiDh7t7Fi8FRYVISnv7lGectgjZCZA4SRK9lzaInyZCqkLqQcVieciLyZBxQy2ZA478NbEDU000XwNBxxZCLrBpbRxHq31mqDSmzWZBCeVZALrY8yLZC0asZBA8OwmWOAZAcPrRs2iShZB605fYJRlm9C5hXviUZD"
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")

friend_list = [friend['name'] for friend in friends['data']]

print friend_list