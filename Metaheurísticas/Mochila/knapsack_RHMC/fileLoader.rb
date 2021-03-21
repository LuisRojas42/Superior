#!/usr/bin/env ruby
def read_file(path)
  files = Dir["#{path}/*.txt"]
  files
end
