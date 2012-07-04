#! /usr/bin/env ruby
# usage: 
# $ das_download.rb email password [download_directory]

require 'mechanize'
# gem 'mechanize-progressbar'

email    = ARGV[0] or raise('Please provide the email address for your account')
password = ARGV[1] or raise('Please provide the password for your account')
path     = ARGV[2] || './' 

download = lambda do |url, file|
  agent = Mechanize.new
  agent.get 'https://www.destroyallsoftware.com/screencasts/users/sign_in'
  form  = agent.page.forms.first
  form['user[email]']    = email
  form['user[password]'] = password
  form.submit
  agent.pluggable_parser.default = Mechanize::Download
  agent.get(url).save(file)
end

agent = Mechanize.new
agent.get 'https://www.destroyallsoftware.com/screencasts/catalog'
screencasts = agent.page.search('li.screencast')

while screencast = screencasts.pop
  title = screencast.search('a').first.text
  url   = screencast.search('.download_link > a:first-child').first['href']
  index = screencasts.size - 1
  file  = "#{path}/#{"%03d" % (index + 1)}-#{title.gsub(/\.|:|,/, '').gsub(/\/|\s/, '-').downcase}.mov"
  puts "Downloading #{title} - #{index} to go"
  next puts 'Already Downloaded' if File.exist? file
  download[url, file]
end
