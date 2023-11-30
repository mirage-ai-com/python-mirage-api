##
# python-mirage-api
#
# Copyright 2023, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

from mirage_api import Mirage

client = Mirage(
  "ui_a311da78-6b89-459c-8028-b331efab20d5",
  "sk_f293d44f-675d-4cb1-9c78-52b8a9af0df2"
)

data = client.task.answer_question({
  "question": "Should I pay more for that?",

  "answer": {
    "start": "Sure,"
  },

  "context": {
    "primary_id": "cf4ccdb5-df44-4668-a9e7-3ab31bebf89b",

    "conversation": {
      "messages": [
        {
          "from": "customer",
          "text": "Hey there!"
        },

        {
          "from": "agent",
          "text": "Hi. How can I help?"
        },

        {
          "from": "customer",
          "text": "I want to add more sub-domains to my website."
        }
      ]
    }
  }
})

print(data)
