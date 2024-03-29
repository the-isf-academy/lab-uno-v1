from simple_term_menu import TerminalMenu

class TerminalView:
    """Handles input and output from a Game.
    You should switch into a different mode while reading this file: here, it's about
    the "skin" the game – like a user interface – whereas over in game.py it's about the
    algorithms and interactions.

    Most important point: The View has no idea what is going on in the game, it
    just give messages for particular events.
    """

# ----------- 💻 PART 1️⃣: EDIT THE CODE HERE ⬇️ -----------

    CARD_ACTION_MESSAGES = {
        "wild-draw-four": "{next_player.name} drew four cards and set the color to {card.color}",
        "draw-two": "{next_player.name} drew two cards!",
        "wild": "{player.name} set the color to {card.color}",
        "skip": "Skipped {next_player.name}!",
        "reverse": "Change directions!",
    }

    def welcome(self):
        print("-"*12)
        print("--- UNO ---")
        print("-"*12,"\n")

    def get_input(self,prompt):
        print(prompt)
        response = input(" >")
        return response

    def menu(self,prompt, options):
        '''This function creates an interactive Terminal menu.'''

        print(prompt)
        terminal_menu = TerminalMenu(options) #Creates the Terminal Menu 
        option_num = terminal_menu.show() #Get user selected Option 

        print(options[option_num],"\n")
        return options[option_num]

    def setup(self):
        print("---- Dealing Cards ----")

    def show_beginning_turn(self, player, top_card):
        print("")
        print("----------------")
        print("The top card is {}.".format(top_card))
        print("----------------")
        print("\n{}, it is your turn.".format(player.name))

    def show_played_card(self, player, card):
        print("{} played {}.".format(player.name, card))

    def show_drawing_card(self, player):
        print("{} drew a card.".format(player.name))

    def show_invalid_card(self, player, card, top_card):
        print("{} can't be played on {}. {} must draw 2 cards.".format(card, top_card, player.name))

    def show_shuffling_deck(self):
        print("Deck is out of cards! Shuffling discard pile.")

    def show_empty_decks(self):
        print("All cards have been dealt! Someone play a card!")

    def show_ending_turn(self, player):
        print("{}, your turn is over.".format(player.name))
        print("----------------")

    def show_winning_game(self, player):
        print("🎉{} WINS!!!🎉".format(player.name))

    def show_out_of_cards(self):
        print("Not enough cards in deck. Ending game.")

    def show_card_action(self, player, next_player, card):
        message = self.CARD_ACTION_MESSAGES[card.special]
        print(message.format(player=player, next_player=next_player, card=card))

    def end_game(self):
        print("-"*25)
        print("-"*25)

