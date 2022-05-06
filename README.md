# IPSync
This project aims to help in automatically syncing devices on local network by fetching the IP address of server from cloud.

When a user logs into a server using IPSync, the server's localIP will be saved on a cloud IPSync instance against user+server project details.

For example, if there is a local project Retro's Utility Server running on 192.168.1.4:4200, then IPSync will save 192.168.1.4.

The user can then log into the client application that connects to the local server and fetch connection details from IPSync.
