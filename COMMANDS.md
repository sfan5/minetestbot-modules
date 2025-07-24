Commands
========
Required arguments are enclosed in &lt; and &gt;, optional arguments are enclosed in [ and ]

<i>$botname</i> refers to the name of the IRC bot, e.g. MinetestBot

<table>
    <tr> <th>Command</th>                            <th>Description</th>                                     <th>Restrictions</th>  </tr>
    <tr> <td><b>admin.py</b></td>                    <td></td>                                                <td></td>              </tr>
    <tr> <td>!join &lt;channel&gt; [key]</td>        <td>Join the specified channel</td>                      <td>Admin-only</td>    </tr>
    <tr> <td>!part &lt;channel&gt;</td>              <td>Leave the specified channel</td>                     <td>Admin-only</td>    </tr>
    <tr> <td>!quit</td>                              <td>Disconnect from IRC server</td>                      <td>Owner-only</td>    </tr>
    <tr> <td>!msg &lt;channel/user&gt; &lt;message&gt;</td><td>Send message to channel or user</td>           <td>Admin-only</td>    </tr>
    <tr> <td>!me &lt;channel/user&gt; &lt;message&gt;</td><td>Send action to channel or user</td>             <td>Admin-only</td>    </tr>
    <tr> <td><b>antiabuse.py</b></td>                <td></td>                                                <td></td>              </tr>
    <tr> <td>!ignore &lt;user&gt;</td>               <td>Add user to ignore list</td>                         <td>Admin-only</td>    </tr>
    <tr> <td>!unignore &lt;user&gt;</td>             <td>Remove user from ignore list</td>                    <td>Admin-only</td>    </tr>
    <tr> <td>!listignore</td>                        <td>List all ignored users</td>                          <td>Admin-only</td>    </tr>
    <tr> <td><b>calc.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!c &lt;expression&gt;</td>              <td>Calculate expression</td>                            <td></td>              </tr>
    <tr> <td><b>chop.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!op [nick] ...</td>                     <td>Op nick (or yourself)</td>                           <td>Admin-only</td>    </tr>
    <tr> <td>!deop [nick] ...</td>                   <td>Deop nick (or yourself)</td>                         <td>Admin-only</td>    </tr>
    <tr> <td>!voice [nick] ...</td>                  <td>Voice nick (or yourself)</td>                        <td>Admin-only</td>    </tr>
    <tr> <td>!devoice [nick] ...</td>                <td>Devoice nick (or yourself)</td>                      <td>Admin-only</td>    </tr>
    <tr> <td>!ban &lt;nick/mask&gt; ...</td>         <td>Ban nick or mask</td>                                <td>Admin-only</td>    </tr>
    <tr> <td>!unban &lt;nick/mask&gt; ...</td>       <td>Unban nick or mask</td>                              <td>Admin-only</td>    </tr>
    <tr> <td>!mute &lt;nick/mask&gt; ...</td>        <td>Mute nick or mask</td>                               <td>Admin-only</td>    </tr>
    <tr> <td>!unmute &lt;nick/mask&gt; ...</td>      <td>Unmute nick or mask</td>                             <td>Admin-only</td>    </tr>
    <tr> <td>!kick &lt;nick&gt; [message]</td>       <td>Kick nick with message</td>                          <td>Admin-only</td>    </tr>
    <tr> <td><b>ping.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>(hi|hello|hey) <i>$botname</i></td>     <td>Reply with (Hi|Hello|Hey)( |!)</td>                  <td></td>              </tr>
    <tr> <td><b>reload.py</b></td>                   <td></td>                                                <td></td>              </tr>
    <tr> <td><i>$botname</i>: reload &lt;module&gt;</td><td>Reloads specified module</td>                     <td>Admin-only</td>    </tr>
    <tr> <td><b>rutils.py</b></td>                   <td></td>                                                <td></td>              </tr>
    <tr> <td>!b64e &lt;string&gt;</td>               <td>Base64-encode a string</td>                          <td></td>              </tr>
    <tr> <td>!b64d &lt;string&gt;</td>               <td>Base64-decode a string</td>                          <td></td>              </tr>
    <tr> <td>!rand [min] &lt;max&gt;</td>            <td>Get a random number inside [min, max]</td>           <td></td>              </tr>
    <tr> <td><b>seen.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!seen &lt;person&gt;</td>               <td>Reports when person was last seen</td>               <td></td>              </tr>
    <tr> <td><b>server.py</b></td>                   <td></td>                                                <td></td>              </tr>
    <tr> <td>!server [query] ...</td>                <td>Search servers from servers.minetest.net</td>        <td></td>              </tr>
    <tr> <td></td>                                   <td><code>addr:&lt;string&gt;</code> searches in Address</td><td></td>          </tr>
    <tr> <td></td>                                   <td><code>name:&lt;string&gt;</code> searches in Server name</td><td></td>      </tr>
    <tr> <td></td>                                   <td><code>players:&lt;modifier&gt;</code> uses Player count</td><td></td>       </tr>
    <tr> <td></td>                                   <td>- most servers with most players</td>                <td></td>              </tr>
    <tr> <td></td>                                   <td>- least servers with least players</td>              <td></td>              </tr>
    <tr> <td></td>                                   <td>- &gt;N servers with less than N players</td>        <td></td>              </tr>
    <tr> <td></td>                                   <td>- &lt;N servers with more than N players</td>        <td></td>              </tr>
    <tr> <td></td>                                   <td>- [=]N servers with exactly N players</td>           <td></td>              </tr>
    <tr> <td></td>                                   <td><code>ping:&lt;modifier&gt;</code> uses Ping</td>    <td></td>              </tr>
    <tr> <td></td>                                   <td>- same modifiers as players:</td>                    <td></td>              </tr>
    <tr> <td></td>                                   <td><code>port:&lt;modifier&gt;</code> uses Port</td>    <td></td>              </tr>
    <tr> <td></td>                                   <td>- same modifiers as players:</td>                    <td></td>              </tr>
    <tr> <td></td>                                   <td><code>i:N/last</code> return server at index N</td>  <td></td>              </tr>
    <tr> <td></td>                                   <td><code>random</code> pick random server (default)</td><td></td>              </tr>
    <tr> <td><b>serverup.py</b></td>                 <td></td>                                                <td></td>              </tr>
    <tr> <td>!up &lt;IP/hostname&gt; [port]</td>     <td>Check if Minetest server is responding</td>          <td></td>              </tr>
    <tr> <td><b>title.py</b></td>                    <td></td>                                                <td></td>              </tr>
    <tr> <td>!title [link]</td>                      <td>Get page title of given URL (or last seen)</td>      <td></td>              </tr>
    <tr> <td><b>shortutils.py</b></td>               <td></td>                                                <td></td>              </tr>
    <tr> <td>!questions [nick]</td>                  <td>Link to ESR's "How to ask smart questions"</td>      <td></td>              </tr>
    <tr> <td>!next</td>                              <td>Say: "Another satisfied customer. Next!"</td>        <td></td>              </tr>
    <tr> <td>!pil [nick]</td>                        <td>Link to Lua PIL and manual</td>                      <td></td>              </tr>
    <tr> <td>!git [nick]</td>                        <td>Link to Git manual</td>                              <td></td>              </tr>
    <tr> <td>!api [nick]</td>                        <td>Link to API docs</td>                                <td></td>              </tr>
    <tr> <td>!btc [currency]</td>                    <td>Get Bitcoin price for specified currency</td>        <td></td>              </tr>
    <tr> <td><b>tell.py</b></td>                     <td></td>                                                <td></td>              </tr>
    <tr> <td>!tell &lt;nick&gt; &lt;message&gt;</td> <td>Tell somebody a message</td>                         <td></td>              </tr>
    <tr> <td><b>modsearch.py</b></td>                <td></td>                                                <td></td>              </tr>
    <tr> <td>!mod &lt;search text&gt;</td>           <td>Searches for a mod</td>                              <td></td>              </tr>
    <tr> <td>!cdb &lt;search text&gt;</td>           <td>Searches for a mod</td>                              <td></td>              </tr>
    <tr> <td><b>booksearch.py</b></td>               <td></td>                                                <td></td>              </tr>
    <tr> <td>!book &lt;term&gt;</td>                 <td>Searches for a chapter/page in the modding book</td> <td></td>              </tr>
</table>
