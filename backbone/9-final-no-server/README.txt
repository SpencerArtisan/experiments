Backbone Tunes: A backbone.js demo
==================================

- Displays a list of available albums and their tracks
- Allows queueing albums for playback
- Plays the queue, one track at a time

USAGE
=====

This version works without the Ruby server.

Drag public/index.html to your web browser.

NOTES
=====

Some changes were required to run this application without a server.

index.html: 

* JSON data must be loaded manually with "reset". 
* The app must be started by calling our custom "home" method on the App router.
* Dynamic hash-based routes won't work.

js/Tunes.js: 

* Some events must be queued with jQuery's 'live' method. See the bottom of PlaylistView's initialize method.


