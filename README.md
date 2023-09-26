# Subject

Transmission of text information via TCP protocol. Tracking the status of
packets.

# Description

Implement a simple server program using the TCP protocol. The server should
support the execution of several commands, determined at the student’s
discretion, but at a minimum should support the execution of the following
(or similar):

 * `ECHO` (returns the data transmitted by the client after the command);

 * `TIME` (returns the current server time);

 * `CLOSE` (closes the connection).

 A command can have parameters (e.g. `ECHO`). Any command must end with the
 characters `\r\n` or `\n`.
