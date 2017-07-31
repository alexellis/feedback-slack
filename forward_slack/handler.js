"use strict"

// Needs a config.json file with slack token for bot etc.
// Sample config at end of file.

let util = require('util')
let fs = require('fs');
let request = require('request');

var bot = {};

let handler = (text, done) => {
  var msg = JSON.parse(text);

  if(msg["bot_name"]) {
      bot.username = msg["bot_name"];
      process.env.slack_name = msg["bot_name"];
  } else {
      bot.username = "faas-bot"
  }

  handle(msg, (err) => {
    if(err) return console.error(err);

    console.log("Done");
    return done(err);
  });
}

let handle = (msg, done) => {
  let req = "";
  if(msg.message.subject && msg.message.subject.length > 0) {
    req = msg.message.subject + " - ";
  }
  req = req + msg.message.body;

  let body = {
     icon_emoji: msg.icon_emoji,
     text: req,
     username: bot.username
  };

  let post = {
    uri: "https://hooks.slack.com/services/" + process.env.slack_incoming_hook,
    json: true,
    body: body
  };

  request.post(post, (err, res, body) => {
    done(err);
  });
};

module.exports = handler;
