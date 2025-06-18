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

# Example 1: Basic chat answer
data = client.task.answer_chat({
  "context": {
    "conversation": {
      "messages": [
        {
          "from": "user",
          "text": "Where is my order?"
        }
      ]
    }
  },
  "model": "medium"
})

print("Basic chat answer:")
print(data)
print("\n" + "="*50 + "\n")

# Example 2: Chat answer with tools
data_with_tools = client.task.answer_chat({
  "context": {
    "conversation": {
      "messages": [
        {
          "from": "user",
          "text": "Where is my order?"
        }
      ]
    }
  },
  "tools": [{
    "type": "function",
    "function": {
      "name": "get-order-details",
      "description": "Retrieves a user order details.",
      "parameters": {
        "type": "object",
        "properties": {
          "email": {
            "type": "string",
            "description": "customer email"
          },
          "order_number": {
            "type": "string",
            "description": "an order number"
          }
        },
        "required": ["email", "order_number"]
      }
    }
  }],
  "model": "medium"
})

print("Chat answer with tools:")
print(data_with_tools)
print("\n" + "="*50 + "\n")
