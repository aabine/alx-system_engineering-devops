#!/usr/bin/env ruby
puts AGRV[0].scan(/\[form:(.*?)\] \[to:(.*?)\] \[flag:(.*?)\]/).join(",")
