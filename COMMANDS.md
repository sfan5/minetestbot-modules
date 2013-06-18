Commands
========
Required arguments are enclosed in { and }, optional arguments are enclosed in \[ and \]

<i>$botname</i> refers to the name of the IRC bot, e.g. MinetestBot

<table>
    <tr> <th>Command</th>                            <th>Description</th>                                     <th>Usable by</th>    </tr>
    <tr> <td><b>admin.py</b></td>                    <td></td>                                                <td></td>              </tr>
    <tr> <td>!join {channel} [channel-key]</td>      <td>Join the specified channel</td>                      <td><i>Admins</i></td> </tr>
    <tr> <td>!part {channel}</td>                    <td>Leave the specified channel</td>                     <td><i>Admins</i></td> </tr>
    <tr> <td>!quit</td>                              <td>Disconnect from IRC Server</td>                      <td><b>Owner</b></td>  </tr>
    <tr> <td><i>$botname</i>: quit</td>              <td>Disconnect from IRC Server</td>                      <td><b>Owner</b></td>  </tr>
    <tr> <td>!msg {channel/user} {message}</td>      <td>Send message to channel/user</td>                    <td><i>Admins</i></td> </tr>
    <tr> <td>!me {channel/user} {message}</td>       <td>Send action to channel/user</td>                     <td><i>Admins</i></td> </tr>
    <tr> <td><b>antiabuse.py</b></td>                <td></td>                                                <td></td>              </tr>
    <tr> <td>!ignore {user}</td>                     <td>Add user to ignore list</td>                         <td><i>Admins</i></td> </tr>
    <tr> <td>!unignore {user}</td>                   <td>Remove user from ignore list</td>                    <td><i>Admins</i></td> </tr>
    <tr> <td><b>calc.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!c {expression}</td>                    <td>Calculate expression using Google Calculator</td>    <td>Anyone</td>        </tr>
    <tr> <td><b>chop.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!op [nick] ...</td>                     <td>Op nick</td>                                         <td><i>Admins</i></td> </tr>
    <tr> <td>!deop [nick] ...</td>                   <td>DeOp nick</td>                                       <td><i>Admins</i></td> </tr>
    <tr> <td>!voice {nick} [nick] ...</td>           <td>Voice nick</td>                                      <td><i>Admins</i></td> </tr>
    <tr> <td>!devoice {nick} [nick] ...</td>         <td>DeVoice nick</td>                                    <td><i>Admins</i></td> </tr>
    <tr> <td>!ban {nick/mask} [nick/mask] ...</td>   <td>Ban nick/mask</td>                                   <td><i>Admins</i></td> </tr>
    <tr> <td>!unban {nick/mask} [nick/mask] ...</td> <td>UnBan nick/mask</td>                                 <td><i>Admins</i></td> </tr>
    <tr> <td>!mute {nick/mask} [nick/mask] ...</td>  <td>Mute nick/mask</td>                                   <td><i>Admins</i></td> </tr>
    <tr> <td>!unmute {nick/mask} [nick/mask]...</td> <td>UnMute nick/mask</td>                                 <td><i>Admins</i></td> </tr>
    <tr> <td>!kick {nick} {message}</td>             <td>Kick nick with message</td>                          <td><i>Admins</i></td> </tr>
    <tr> <td>!badword {on/off/reload}</td>           <td>Enable/Disable badword functionality</td>            <td><i>Admins</i></td> </tr>
    <tr> <td><b>forumutils.py</b></td>               <td></td>                                                <td></td>              </tr>
    <tr> <td>!sfu {searchstring}</td>                <td>Search Minetest Forum users using searchstring</td>  <td>Anyone</td>        </tr>
    <tr> <td>!sfulimit {user} {'reset'/number}</td>  <td>Set search limit for user</td>                       <td><i>Admins</i></td> </tr>
    <tr> <td><b>ping.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>(hi|hello|hey) <i>$botname</i></td>     <td>Reply with (Hi|Hello|Hey)( |!)</td>                  <td>Anyone</td>        </tr>
    <tr> <td><b>reload.py</b></td>                   <td></td>                                                <td></td>              </tr>
    <tr> <td><i>$botname</i>: reload {module}</td>   <td>Reloads specified module</td>                        <td><i>Admins</i></td> </tr>
    <tr> <td><b>rutils.py</b></td>                   <td></td>                                                <td></td>              </tr>
    <tr> <td>!rev {string}</td>                      <td>Reverse String</td>                                  <td>Anyone</td>        </tr>
    <tr> <td>!b64e {string}</td>                     <td>Base64-encode a string</td>                          <td>Anyone</td>        </tr>
    <tr> <td>!b64d {string}</td>                     <td>Base64-decode a string</td>                          <td>Anyone</td>        </tr>
    <tr> <td>!b32e {string}</td>                     <td>Base32-encode a string</td>                          <td>Anyone</td>        </tr>
    <tr> <td>!b32d {string}</td>                     <td>Base32-decode a string</td>                          <td>Anyone</td>        </tr>
    <tr> <td>!b16e {string}</td>                     <td>Base16-encode a string</td>                          <td>Anyone</td>        </tr>
    <tr> <td>!b16d {string}</td>                     <td>Base16-decode a string</td>                          <td>Anyone</td>        </tr>
    <tr> <td>!crc32 {string}</td>                    <td>Hash a string using crc32</td>                       <td>Anyone</td>        </tr>
    <tr> <td>!hex {string}</td>                      <td>"Hexlify" a string</td>                              <td>Anyone</td>        </tr>
    <tr> <td>!unhex {string}</td>                    <td>Un-"Hexlify" a string</td>                           <td>Anyone</td>        </tr>
    <tr> <td>!uuencode {string}</td>                 <td>uuencode a string</td>                               <td>Anyone</td>        </tr>
    <tr> <td>!uudecode {string}</td>                 <td>uudecode a string</td>                               <td>Anyone</td>        </tr>
    <tr> <td>!re {regex}<i>`</i>{string}</td>        <td>check if regex matches, if it does print groups</td> <td>Anyone</td>        </tr>
    <tr> <td><b>search.py</b></td>                   <td></td>                                                <td></td>              </tr>
    <tr> <td>!g {string}</td>                        <td>Output first Google result for string</td>           <td>Anyone</td>        </tr>
    <tr> <td>!gc {string}</td>                       <td>Output Google result count for string</td>           <td>Anyone</td>        </tr>
    <tr> <td><b>seen.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!seen {person}</td>                     <td>Output when person was last seen</td>                <td>Anyone</td>        </tr>
    <tr> <td><b>server.py</b></td>                   <td></td>                                                <td></td>              </tr>
    <tr> <td>!server [query] [query] ...</td>        <td>Search servers at servers.minetest.net</td>          <td>Anyone</td>        </tr>
    <tr> <td></td>                                   <td>addr:{string} searches in Address</td>               <td></td>              </tr>
    <tr> <td></td>                                   <td>name:{string} searches in Server name</td>           <td></td>              </tr>
    <tr> <td></td>                                   <td>players:{modifier} uses Player count</td>            <td></td>              </tr>
    <tr> <td></td>                                   <td>- most finds servers with most players</td>          <td></td>              </tr>
    <tr> <td></td>                                   <td>- least finds servers with least players</td>        <td></td>              </tr>
    <tr> <td></td>                                   <td>- >{number} finds servers with players > x</td>      <td></td>              </tr>
    <tr> <td></td>                                   <td>- &lt;{num} finds servers with players &lt; x</td>   <td></td>              </tr>
    <tr> <td></td>                                   <td>- [=]{number} finds servers with x players</td>      <td></td>              </tr>
    <tr> <td></td>                                   <td>- !{number} finds servers with not x players</td>    <td></td>              </tr>
    <tr> <td></td>                                   <td>ping:{modifier} uses Player count</td>               <td></td>              </tr>
    <tr> <td></td>                                   <td>- same modifiers as players:</td>                    <td></td>              </tr>
    <tr> <td></td>                                   <td>port:{modifier} uses Port</td>                       <td></td>              </tr>
    <tr> <td></td>                                   <td>- same modifiers as players:</td>                    <td></td>              </tr>
    <tr> <td></td>                                   <td>i:{number/'last'} return Server no. x</td>           <td></td>              </tr>
    <tr> <td></td>                                   <td>random pick random entry from results</td>           <td></td>              </tr>
    <tr> <td><b>serverup.py</b></td>                 <td></td>                                                <td></td>              </tr>
    <tr> <td>!up {IP/hostname} [port]</td>           <td>Check if server at IP/hostname is up</td>            <td>Anyone</td>        </tr>
    <tr> <td></td>                                   <td>Supports multiple Ports e.g. 123-456,999</td>        <td></td>              </tr>
    <tr> <td><b>shorten.py</b></td>                  <td></td>                                                <td></td>              </tr>
    <tr> <td>!sh {service} {url}</td>                <td>Shortens URL</td>                                    <td>Anyone</td>        </tr>
    <tr> <td></td>                                   <td>Currently supports: id.gd, v.gd</td>                 <td></td>              </tr>
    <tr> <td><b>title.py</b></td>                    <td></td>                                                <td></td>              </tr>
    <tr> <td>!title [link]</td>                      <td>Query Page Title</td>                                <td>Anyone</td>        </tr>
    <tr> <td><b>twitter.py</b></td>                  <td></td>                                                <td></td>              </tr>
    <tr> <td>!tw {link/username/tweet_id}</td>       <td>Query Tweet from Twitter</td>                        <td>Anyone</td>        </tr>
    <tr> <td><b>wiki.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!wik {term}</td>                        <td>Query wiki.minetest.com for term</td>                <td>Anyone</td>        </tr>
    <tr> <td><b>devwiki.py</b></td>                  <td></td>                                                <td></td>              </tr>
    <tr> <td>!dev {term}</td>                        <td>Query dev.minetest.net for term</td>                 <td>Anyone</td>        </tr>
</table>
