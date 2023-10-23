##
# python-mirage-api
#
# Copyright 2023, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class TaskResource(object):
  def __init__(self, parent):
    self.parent = parent

  def transcribe_speech(self, data):
    return self.parent.post("/task/transcribe/speech", data)

  def answer_question(self, data):
    return self.parent.post("/task/answer/question", data)

  def summarize_paragraphs(self, data):
    return self.parent.post("/task/summarize/paragraphs", data)

  def summarize_conversation(self, data):
    return self.parent.post("/task/summarize/conversation", data)

  def categorize_conversations(self, data):
    return self.parent.post("/task/categorize/conversations", data)

  def rank_question(self, data):
    return self.parent.post("/task/rank/question", data)

  def translate_text(self, data):
    return self.parent.post("/task/translate/text", data)
