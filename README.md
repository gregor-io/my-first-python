# my-first-python
I have only been programming for about 2 months now, and I am trying to learn! Any help would be appreciated! 

This is my first Python project with data structures. I had my program "read" the Bible and organize it into a dictionary.

I am really just looking for suggestions on better ways to organize the data that I collected from the Bible. The dictionary is organized as follows:
  {word: [number, {word2:} ] }
  The key is a word that is found in the text. The value is a list, with 2 positions. Position 0 is the amount of times that the program encounted the word, and position 1 is a dictionary of all the words that followed the keyword. The key of the second dictionary is the word and the value is how many times that subkey followed the original keyword.
  
  {the:[10, {book:2}]} means that "the" was encountered 10 times, and that the word "book" AFTER the word "the" was encountered 2 times.
  
  My main goal was to have the program take the dictionary in total and develop a sentence based on what it "read" from the Bible (or other texts as I add them), but I wasn't sure the best way to have it randomly generate sentences that would be gramatically correct. Looking for any help as I begin my journey into the CS world!
