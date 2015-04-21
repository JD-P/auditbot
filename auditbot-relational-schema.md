Database Schema for Auditbot:
=============================

Networks(id, nwid)
----
Dependencies:

server -> nwid

server (int) PRIMARY FOREIGN KEY OF Servers(id) - The id of a server associated with the nwid.

nwid (int) UNIQUE - A unique integer id associated with the name of the network.

nw_name (text) UNIQUE - The name of an IRC network, must be unique.


Servers(id, hostname, nwid)
---
Dependencies:

hostname -> id

Schema:

id (int) PRIMARY KEY - A unique integer associated with the hostname.

hostname (text) UNIQUE - The hostname of the server.


Nicks(id, nick):
---
Dependencies:

id -> nick

Schema:

id (int) PRIMARY KEY - A unique integer associated with the nick.

nick (text) UNIQUE - The nickname associated with the id.


Users(id, username):
---
Dependencies:

id -> username

Schema:

id (int) PRIMARY KEY - A unique integer associated with the user of the hostmask.

username (text) UNIQUE - The system username associated with the user.


Client_Hosts(id, hostname):
---
Dependencies:

id -> hostname

Schema:

id (int) PRIMARY KEY - A unique integer associated with the hostname fo the hostmask.

hostmask (text) UNIQUE - The hostname of the hostmask.


Channels(id, nwid, channel):
---
Dependencies:

id -> nwid, channel

Schema:

id (int) PRIMARY KEY - A unique integer associated with the channel.

nwid (int) FOREIGN KEY OF Networks(nwid) - The IRC network the channel is on.

channel (text) - The channel name.

UNIQUE (nwid, channel)


Msg_Types(id, type)
---
Dependencies:

id -> type

Schema:

id (int) PRIMARY KEY - A unique integer associated with the message type.

type (text) UNIQUE - A string representing the type of message.


Hostmasks(id, nwid, nickname, user, hostname)
---
Dependencies:

id -> server, nickname, user, hostname

Schema:

id (int) PRIMARY KEY - A unique integer associated with the hostmask.

nwid (int) - The integer id of the IRC network the hostname is associated with.

nickname (int) FOREIGN KEY OF Nicks(id) - An id representing a users nick.

user (text) FOREIGN KEY OF Users(id) - An id representing the 'user' part of a hostmask.

hostname (text) FOREIGN KEY OF Client_Hosts(id) - An id representing the hostname part of a hostmask.

UNIQUE (server, nickname, user, hostname)


Registered(nwid, nickname, time_of, account)
---
Dependencies:

nwid, nickname -> nwid, account, time_of

Schema:

nwid (int) FOREIGN KEY OF Networks(id) - An id representing the network this nick was registered on.

nickname (int) FOREIGN KEY OF Nicks(id) - An id representing a users nick.

time_of (int | timestamp) - The date and time that the nick was registered.

account (int) FOREIGN KEY OF Nicks(id) - The account under which the nick was registered.

PRIMARY KEY (nwid, nickname, registered)


Messages(id, timestamp, channel, type)
----
Dependencies:

id -> timestamp, channel, type

Schema:

id (integer) PRIMARY KEY - A unique identification number for every message sent by the IRC server.

timestamp (int) - A timestamp for every message in the database.

channel (int) FOREIGN KEY OF Channels(id) - The name of the channel, server or user from which the message originated.

type (int) FOREIGN KEY OF Msg_Types(id) - The type of message, possible types of message are PRIVMSG, NOTICE, JOIN, PART, QUIT, KICK, NICK, SETMODE, TOPIC.


Privmsgs(id, nickname, message)
----
Dependencies:

id -> nickname, message

Schema:

id (integer) FOREIGN KEY OF Messages(id) - A unique identification number for every message sent by the IRC server.

nickname (int) FOREIGN KEY OF Nicks(id) - An integer representing a users nick.

message (text) - The PRIVMSG sent to the channel or user.


Notices(id, nickname, message)
----
Dependencies:

id -> nickname, message

Schema:

id (integer) FOREIGN KEY OF Messages(id) - A unique identification number for every message sent by the IRC server.

nickname (int) FOREIGN KEY OF Nicks(id) - An integer representing a users nick.

message (text) - The NOTICE sent to the channel or user.


Joins(id, hostmask)
----
Dependencies:

id -> hostmask

Schema:

id (integer) PRIMARY FOREIGN KEY OF Messages(id) - A unique identification number for every message sent by the IRC server.

hostmask (integer) FOREIGN KEY OF Hostmasks(id) - The hostmask that joined.


Parts(id, hostmask, part_message)
----
Dependencies:

id -> hostmask, part_message

Schema:

id (integer) FOREIGN KEY OF Messages(id) - A unique identification number for every message sent by the IRC server.

hostmask (int) FOREIGN KEY OF Hostmasks(id) - The hostmask that parted.

part_message (text) - The parting message sent by the client.


Quits(id, hostmask, quit_message)
----
Dependencies:

id -> hostmask, quit_message

Schema:

id (integer) FOREIGN KEY OF Messages(id) - A unique identification number for every message sent by the IRC server.

hostmask (int) FOREIGN KEY OF Hostmasks(id) - The hostmask that quit.

quit_message (text) - The quit message sent by the client.


Kicks(id, nick_kicked, kicked_by, kick_message)
----
Dependencies:

id -> nick_kicked, kicked_by, kick_message

Schema:

id (integer) FOREIGN KEY OF Messages(id) - A unique identification number for every message sent by the IRC server.

nick_kicked (int) FOREIGN KEY OF Nicks(id) - The nick of the user kicked from channel.

kicked_by (int) FOREIGN KEY OF Nicks(id) - The nick of the operator that kicked the user.

kick_message (text) - The message the operator wrote as justification for the kick.


Nick_Changes(id, nick_before, nick_after)
----
Dependencies:

id -> nick_before, nick_after

Schema:

id (integer) PRIMARY FOREIGN KEY OF Messages(id) - A unique identification number for every message sent by the IRC server.

nick_before (id) FOREIGN KEY OF Nicks(id) - The users nick before the change.

nick_after (id) FOREIGN KEY OF Nicks(id) - The users nick after the change.


Setmodes(id, set_by, mode_string)
----
Dependencies:

id -> set_by, mode_string

Schema:

id (integer) FOREIGN KEY OF Messages(id) - A unique identification number for every message sent by the IRC server.

set_by (int) FOREIGN KEY OF Nicks(id) - The nickname of the operator who set the mode for the channel.

mode_string (text) - The mode set.


Topics(id, changed_by, topic)
----
Dependencies:

id -> changed_by, topic

Schema:

id (integer) PRIMARY FOREIGN KEY OF Messages(id) - A unique identification number for every message sent by the IRC server.

changed_by (int) FOREIGN KEY OF Nicks(id) - The nick of the user that changed the topic.

topic (text) - The text of the new topic for the channel.

Errata:
-------

Nickserv identify temporarily binds a connection to an account. (Here a connection would be a user@hostname combo.)
