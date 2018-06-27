Commands
========
Required arguments are enclosed in { and }, optional arguments are enclosed in [ and ]

<i>$botname</i> refers to the name of the IRC bot, e.g. MinetestBot

<table>
    <tr> <th>Command</th>                            <th>Description</th>                                     <th>Usable by</th>     </tr>
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
    <tr> <td>!listignore</td>                        <td>List all ignored users</td>                          <td><i>Admins</i></td> </tr>
    <tr> <td><b>calc.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!c {expression}</td>                    <td>Calculate expression</td>                            <td>Anyone</td>        </tr>
    <tr> <td><b>chop.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!op [nick] ...</td>                     <td>Op nick</td>                                         <td><i>Admins</i></td> </tr>
    <tr> <td>!deop [nick] ...</td>                   <td>DeOp nick</td>                                       <td><i>Admins</i></td> </tr>
    <tr> <td>!voice [nick] ...</td>                  <td>Voice nick</td>                                      <td><i>Admins</i></td> </tr>
    <tr> <td>!devoice [nick] ...</td>                <td>DeVoice nick</td>                                    <td><i>Admins</i></td> </tr>
    <tr> <td>!ban {nick/mask} [nick/mask] ...</td>   <td>Ban nick/mask</td>                                   <td><i>Admins</i></td> </tr>
    <tr> <td>!unban {nick/mask} [nick/mask] ...</td> <td>UnBan nick/mask</td>                                 <td><i>Admins</i></td> </tr>
    <tr> <td>!mute {nick/mask} [nick/mask] ...</td>  <td>Mute nick/mask</td>                                  <td><i>Admins</i></td> </tr>
    <tr> <td>!unmute {nick/mask} [nick/mask]...</td> <td>UnMute nick/mask</td>                                <td><i>Admins</i></td> </tr>
    <tr> <td>!kick {nick} [message]</td>             <td>Kick nick with message</td>                          <td><i>Admins</i></td> </tr>
    <tr> <td><b>ping.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>(hi|hello|hey) <i>$botname</i></td>     <td>Reply with (Hi|Hello|Hey)( |!)</td>                  <td>Anyone</td>        </tr>
    <tr> <td><b>reload.py</b></td>                   <td></td>                                                <td></td>              </tr>
    <tr> <td><i>$botname</i>: reload {module}</td>   <td>Reloads specified module</td>                        <td><i>Admins</i></td> </tr>
    <tr> <td><b>rutils.py</b></td>                   <td></td>                                                <td></td>              </tr>
    <tr> <td>!rev {string}</td>                      <td>Reverse String</td>                                  <td>Anyone</td>        </tr>
    <tr> <td>!b64e {string}</td>                     <td>Base64-encode a string</td>                          <td>Anyone</td>        </tr>
    <tr> <td>!b64d {string}</td>                     <td>Base64-decode a string</td>                          <td>Anyone</td>        </tr>
    <tr> <td>!rand [min] {max}</td>                  <td>Says a random number between(incl.) min and max</td> <td>Anyone</td>        </tr>
    <tr> <td><b>seen.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!seen {person}</td>                     <td>Reports when person was last seen</td>               <td>Anyone</td>        </tr>
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
    <tr> <td><b>title.py</b></td>                    <td></td>                                                <td></td>              </tr>
    <tr> <td>!title [link]</td>                      <td>Query Page Title</td>                                <td>Anyone</td>        </tr>
    <tr> <td><b>wiki.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!wik {term}</td>                        <td>Query wiki.minetest.com for term</td>                <td>Anyone</td>        </tr>
    <tr> <td><b>devwiki.py</b></td>                  <td></td>                                                <td></td>              </tr>
    <tr> <td>!dev {term}</td>                        <td>Query dev.minetest.net for term</td>                 <td>Anyone</td>        </tr>
    <tr> <td><b>shortutils.py</b></td>               <td></td>                                                <td></td>              </tr>
    <tr> <td>!rtfm [nick]</td>                       <td>Give links to wiki and dev wiki</td>                 <td>Anyone</td>        </tr>
    <tr> <td>!questions [nick]</td>                  <td>Link to ESR's "How to ask smart questions"</td>      <td>Anyone</td>        </tr>
    <tr> <td>!next</td>                              <td>Say: "Another satisfied customer. Next!"</td>        <td>Anyone</td>        </tr>
    <tr> <td>!pil [nick]</td>                        <td>Link to Lua PIL</td>                                 <td>Anyone</td>        </tr>
    <tr> <td>!git [nick]</td>                        <td>Link to Git manual</td>                              <td>Anyone</td>        </tr>
    <tr> <td>!api [nick]</td>                        <td>Link to API docs</td>                                <td>Anyone</td>        </tr>
    <tr> <td>!btc [currency]</td>                    <td>Get Bitcoin price for specified currency</td>        <td>Anyone</td>        </tr>
    <tr> <td><b>tell.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!tell {nick} {message}</td>             <td>Tell somebody a message</td>                         <td>Anyone</td>        </tr>
    <tr> <td><b>modsearch.py</b></td>                <td></td>                                                <td></td>              </tr>
    <tr> <td>!mod {modname}</td>                     <td>Searches for a mod</td>                              <td>Anyone</td>        </tr>
    <tr> <td><b>booksearch.py</b></td>               <td></td>                                                <td></td>              </tr>
    <tr> <td>!book {term}</td>                       <td>Searches for a chapter/page in the modding book</td> <td>Anyone</td>        </tr>
</table>
