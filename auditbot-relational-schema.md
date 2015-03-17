Database Schema for Auditbot:
=============================

Hostmasks(nickname, user, hostname)
---
Dependencies:

nickname, user, hostname -> nickname, user, hostname

Schema:

nickname (text) - A string representing a users nick.

user (text) - A string representing the 'user' part of a hostmask.

hostname (text) - A string representing the hostname part of a hostmask.

Registered(nickname, registered, account)
---
Dependencies:

nickname -> account

Schema:

nickname (text) - A string representing a users nick.

registered (datetime) - The date and time that the nick was registered.

account (text) - The account under which the nick was registered.

Privmsgs(id, nickname, message)
----
Dependencies:

id -> nickname, message

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

nickname (text) - A string representing a users nick.

message (text) - The PRIVMSG sent to the channel or user.

Notices(id, nickname, message)
----
Dependencies:

id -> nickname, message

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

nickname (text) - A string representing a users nick.

message (text) - The NOTICE sent to the channel or user.

Joins(id, nickname, user, hostname)
----
Dependencies:

id -> nickname, user, hostname

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

nickname (text) - A string representing a users nick.

user (text) - A string representing the 'user' part of a hostmask.

hostname (text) - A string representing the hostname part of a hostmask.

Parts(id, nickname, user, hostname, part_message)
----
Dependencies:

id -> nickname, user, hostname, part_message

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

nickname (text) - A string representing a users nick.

user (text) - A string representing the 'user' part of a hostmask.

hostname (text) - A string representing the hostname part of a hostmask.

part_message (text) - The parting message sent by the client.

Quits(id, nickname, user, hostname, quit_message)
----
Dependencies:

id -> nickname, user, hostname, quit_message

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

nickname (text) - A string representing a users nick.

user (text) - A string representing the 'user' part of a hostmask.

hostname (text) - A string representing the hostname part of a hostmask.

quit_message (text) - The quit message sent by the client.

Kicks(id, nick_kicked, kicked_by, kick_message)
----
Dependencies:

id -> nick_kicked, kicked_by, kick_message

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

nick_kicked (text) - The nick of the user kicked from channel.

kicked_by (text) - The nick of the operator that kicked the user.

kick_message (text) - The message the operator wrote as justification for the kick.

Nick_Changes(id, nick_before, nick_after)
----
Dependencies:

id -> nick_before, nick_after

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

nick_before (text) - The users nick before the change.

nick_after (text) - The users nick after the change.

Setmodes(id, set_by, mode_string)
----
Dependencies:

id -> set_by, mode_string

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

set_by (text) - The nickname of the operator who set the mode for the channel.

mode_string (text) - The mode set.

Topics(id, changed_by, topic)
----
Dependencies:

id -> changed_by, topic

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

changed_by (text) - The nick of the user that changed the topic.

topic (text) - The text of the new topic for the channel.

Messages(id, timestamp, channel, type)
----
Dependencies:

id -> timestamp, channel, type

Schema:

id (integer) - A unique identification number for every message sent by the IRC server.

timestamp (datetime) - A timestamp for every message in the database.

channel (text) - The name of the channel, server or user from which the message originated.

type (text) - The type of message, possible types of message are PRIVMSG, NOTICE, JOIN, PART, QUIT, KICK, NICK, SETMODE, TOPIC.

Errata:
-------

Nickserv identify temporarily binds a connection to an account. (Here a connection would be a user@hostname combo.)
