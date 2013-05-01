def help(phenny, input): 
   """Help command"""
   for x in phenny.bot.commands["high"].values():
      if x[0].__name__ == "aa_hook":
         if x[0](phenny, input):
            return # Abort function
   phenny.say("https://github.com/sfan5/minetestbot-modules/blob/master/COMMANDS.md")

help.commands = ['help']
