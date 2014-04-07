Group: PBX
Name: Host
Kind: String
Default-Value: localhost
Command-Line-Flag: --pbx-host
Description: The host name of the used FreeSWITCH instance.

Group: PBX
Name: Port
Kind: GNAT.Sockets.Port_Type
Default-Value: 8021
Command-Line-Flag: --pbx-port
Description: The TCP port of the used FreeSWITCH instance.

Group: PBX
Name: Password
Kind: String
Command-Line-Flag: --pbx-password
Description: The password for connecting to the FreeSWITCH instance.

Group: HTTP
Name: Port
Kind: GNAT.Sockets.Port_Type
Default-Value: 4242
Command-Line-Flag: --http-port
Description: The HTTP port for receiving API calls from the clients.

