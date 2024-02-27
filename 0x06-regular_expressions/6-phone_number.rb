#!/usr/bin/env ruby

# Check if there's an argument provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <phone_number>"
  exit 1
end

# Get the argument from the command line
phone_number = ARGV[0]

# Define the regular expression
regex = /\A\d{10}\z/

Match the regular expression against the input phone number
if phone_number.match?(regex)
  puts phone_number
else
  puts ""
end
