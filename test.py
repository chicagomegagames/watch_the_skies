#!/usr/bin/env python3
import nose
from os import environ

if __name__ == '__main__':
  environ["APP_ENV"] = "testing"

  nose.run()
