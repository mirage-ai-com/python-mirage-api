##
# python-mirage-api
#
# Copyright 2023, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

class DataResource(object):
  def __init__(self, parent):
    self.parent = parent

  def context_ingest(self, data):
    return self.parent.post("/data/context/ingest", data)
