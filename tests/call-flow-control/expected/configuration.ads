with GNAT.Sockets;

package Configuration is
   package PBX is
      function Host return String;
      function Port return GNAT.Sockets.Port_Type;
      function Secret return String;
   end PBX;

   package HTTP is
      function Port return GNAT.Sockets.Port_Type;
   end HTTP;
end Configuration;
