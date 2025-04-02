##
# python-mirage-api
#
# Copyright 2023, Valerian Saliou
# Author: Valerian Saliou <valerian@valeriansaliou.name>
##

import json
from urllib import request, parse, error
from base64 import b64encode as b64

from .resources.task import TaskResource
from .resources.data import DataResource

class Mirage(object):
  def __init__(self, user_id, secret_key):
    self.__auth = {
      "user_id": user_id,
      "secret_key": secret_key
    }

    self.__rest_host = None
    self.__rest_base_path = None
    self.__timeout = None

    self.task = TaskResource(self)
    self.data = DataResource(self)

  def get_rest_host(self):
    return self.__rest_host or "https://api.mirage-ai.com"

  def get_rest_base_path(self):
    return self.__rest_base_path or "/v1"

  def get_timeout(self):
    return self.__timeout or 40

  def set_rest_host(self, rest_host):
    self.__rest_host = rest_host

  def set_rest_base_path(self, rest_base_path):
    self.__rest_base_path = rest_base_path

  def set_timeout(self, timeout):
    self.__timeout = timeout

  def post(self, resource, data):
    return self.__do_post(resource, data)

  def __do_post(self, resource, data=None, query=None):
    # Fallback on default values (as needed)
    data = data or {}
    query = query or {}

    # Prepare REST URL
    if bool(query) is True:
      url = "%s?%s" % (self.__prepare_rest_url(resource), parse.urlencode(query))
    else:
      url = self.__prepare_rest_url(resource)

    # Convert data to body string
    body = str(json.dumps(data)).encode("utf-8")

    # Generate request headers
    headers = {
      "Content-Type": "application/json",
      "User-Agent": "python-mirage-api/1.7.0",
      "Authorization": self.__generate_auth()
    }

    # Open POST request
    req = request.Request(url, data=body, headers=headers, method="POST")

    try:
      with request.urlopen(req, None, self.get_timeout()) as response:
        data = response.read()
        status = response.code
        raised_error = None
    except error.HTTPError as e:
      data = e.read()
      status = e.code
      response = None
      raised_error = e

    # Raise intercepted error?
    if raised_error:
      raise raised_error

    return json.loads(data) if data else None

  def __generate_auth(self):
    raw = "%s:%s" % (self.__auth["user_id"], self.__auth["secret_key"])
    key = b64(raw.encode("ascii"))

    return "Basic %s" % key.decode("ascii")

  def __prepare_rest_url(self, resource):
    return self.get_rest_host() + self.get_rest_base_path() + resource
